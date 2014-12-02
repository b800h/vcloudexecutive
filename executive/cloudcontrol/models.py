from django.db import models

# Create your models here.
class Actions(models.Model):
    vm_id = models.CharField(max_length=30)
    progress = models.CharField(max_length=30)