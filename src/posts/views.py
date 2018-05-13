from django.shortcuts import render,get_object_or_404

# Create your views here.
from .models import post

def post_list_view(request):
	querySet = post.objects.all()
	context = {
		'object_list':querySet
	}
	return render (request, "posts/list.html", context)


