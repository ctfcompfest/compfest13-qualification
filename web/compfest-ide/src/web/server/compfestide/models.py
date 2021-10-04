from django.db import models

class JobQueue(models.Model):
    code_id = models.CharField(max_length=20)
    code = models.TextField(null=False)
    out = models.TextField(null=True)
    err = models.TextField(null=True)
    status = models.BooleanField(default=False)