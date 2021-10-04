from compfestide.models import JobQueue
from random import choice
from string import ascii_letters, digits
import os

VALID_CHAR = ascii_letters + digits
CODE_DIR = os.getenv('CODE_DIR', '/tmp/code')
SANDBOX_DIR = os.getenv('SANDBOX_DIR', '/tmp/sandbox')
BLACKLIST = ['sh', 'cat', 'ls', 'cd', 'nc', 'wget', 'sleep', 'pwd', '*', '?', '..', '`', '>', '<', '$', '{', '}', '(', ')', ';', '&', '|', '~']

def generate_id(n):
    ret = [choice(VALID_CHAR) for _ in range(n)]
    return ''.join(ret)

def get_output(code_id):
    jobs = JobQueue.objects.filter(code_id = code_id).order_by('pk')
    last_job = jobs.last()
    sz = jobs.count()
    for i in range(sz - 1):
        if jobs[i].status == True: jobs[i].delete()
    return last_job.status, last_job.out, last_job.err

def run_code(code_id):
    job = JobQueue()
    job.code_id = code_id
    with open(f'{CODE_DIR}/{code_id}', 'r') as f:
        job.code = f.read().strip()
    job.save()