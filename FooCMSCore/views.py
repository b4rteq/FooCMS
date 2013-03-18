from django.http import HttpResponse
from django.template.response import TemplateResponse
from FooCMSCore.models import Page, PageLayout, ContentBox
from FooCMS_SimpleContents import views as SimpleContentsViews

def handle_no_such_page(request, page_name):
	return HttpResponse('No such page')

def handle_page_request(request, page_name):

	requested_page = Page.objects.filter(name=page_name)
	if not requested_page:
		return handle_no_such_page(request, page_name)

	page_layout = requested_page[0].pageLayout
	layout_content_boxes = page_layout.contentbox_set.order_by('content_level', 'pk').all()

	return TemplateResponse(request, 'FooCMSCore/content_page.html',{'content_boxes_groups' : prepare_groups(layout_content_boxes)})

def prepare_groups(content_boxes):
	level = -1
	result = []
	for box in content_boxes:
		if box.content_level != level:
			result.append([])
		box.Content = prepare_content(box)
		result[len(result)-1].append(box)
		level = box.content_level
	return result

def prepare_content(content_box):
	content_type_name = type(content_box.content_object).__name__
	return SimpleContentsViews.GetPreparedContent(content_box.content_object, content_type_name)




