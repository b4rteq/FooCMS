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


class NavigationContent(models.Model):
	NAVIGATION_TYPE_CHOICES = (
			(1,"Vertical"),
			(2, "Horizontal")
		)

	name = models.CharField(max_length=15)
	type = models.IntegerField(choices=NAVIGATION_TYPE_CHOICES)

class NavigationLink(models.Model):
	name = models.CharField(max_length=15)
	url = models.CharField(max_length=256)
	priority = models.IntegerField()
	navigationContent = models.ForeignKey(NavigationContent)



