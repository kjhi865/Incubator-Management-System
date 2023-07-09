from django.db import models

# Create your models here.
class start_foun(models.Model):
    startup_id=models.CharField(max_length=20)
    founders_name=models.IntegerField()
