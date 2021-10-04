from compfestide.models import JobQueue
from compfestide.utils import generate_id, SANDBOX_DIR
from pathlib import Path
from subprocess import Popen, PIPE
import json
import os
import time

def run():
    os.setuid(0)
    os.setgid(0)
    os.chdir(SANDBOX_DIR)
    os.chroot(SANDBOX_DIR)
    while True:
        try:
            pending_jobs = JobQueue.objects.filter(status = False)
            sz = pending_jobs.count()
            for i in range(sz):
                job = pending_jobs[i]

                runner_id = generate_id(10)
                with open(runner_id, 'w') as f:
                    f.write(job.code)

                cmd = f'sh {runner_id}'
                out, err = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE).communicate()

                job.out = out.decode()
                job.err = err.decode()
                job.status = True
                job.save()

                print(f"[Done] {job.code_id} - {runner_id}")
                os.remove(runner_id)
        except Exception as ex:
            print(ex)
        time.sleep(0.1)