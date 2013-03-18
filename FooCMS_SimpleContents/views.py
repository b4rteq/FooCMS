from django.template.response import TemplateResponse
from FooCMS_SimpleContents.models import StaticContent, ImageContent
from django.template.loader import render_to_string


def GetPreparedContent(content_object, content_type_name):
	if content_type_name == "StaticContent":
		return content_object.body
	elif content_type_name == "ImageContent":
		return '<img src="/' + content_object.image.name + '"/>'
	elif content_type_name == "NavigationContent":	
		return PrepareNavigationContent(content_object)
	else:
		return "Content not found"

def PrepareNavigationContent(navigation_content):
	links = {"links" : navigation_content.navigationlink_set.all()}
	if navigation_content.type == 1:
		response = render_to_string('FooCMS_SimpleContents/navigation_content_vertical.html', links)
	else:
		response = render_to_string('FooCMS_SimpleContents/navigation_content_horizontal.html', links)

	return response
