from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class PageLayout(models.Model):
	test = models.CharField(max_length=1)


class ContentBox(models.Model):
	CONTENT_SIZE_CHOICES = (
			(1, '1'),
			(2, '2'),
			(3, '3'),
			(4, '4'),
			(5, '5'),
			(6, '6'),
			(7, '7'),
			(8, '8'),
			(9, '9'),
			(10, '10'),
			(11, '11'),
			(12, '12'),
		)

	content_level = models.IntegerField()
	is_empty = models.BooleanField()
	content_size = models.IntegerField(choices=CONTENT_SIZE_CHOICES)
	pageLayout = models.ForeignKey(PageLayout)
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = generic.GenericForeignKey('content_type', 'object_id')



class Page(models.Model):
	name = models.CharField(max_length=15, unique=True)
	pageLayout = models.OneToOneField(PageLayout)
	


