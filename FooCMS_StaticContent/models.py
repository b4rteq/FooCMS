from django.db import models

# Create your models here.


class Instance(models.Model):
	name = models.CharField(max_length=15)
	
