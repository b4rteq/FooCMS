from django.db import models

class StaticContent(models.Model):
	name = models.CharField(max_length=15)
	body = models.TextField()


class ImageContent(models.Model):
	name = models.CharField(max_length=15)
	image = models.ImageField(upload_to="static/ImageContentImages")