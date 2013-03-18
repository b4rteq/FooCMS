from django.db import models

class StaticContent(models.Model):
	name = models.CharField(max_length=15)
	body = models.TextField()

	def __unicode__(self):
		return self.name


class ImageContent(models.Model):
	name = models.CharField(max_length=15)
	image = models.ImageField(upload_to="static/ImageContentImages")

	def __unicode__(self):
		return self.name