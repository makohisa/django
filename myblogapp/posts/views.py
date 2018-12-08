from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Post

#from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

class IndexView(generic.ListView):
	"""docstring for IndexView"""
	template_name = 'posts/index.html'
	context_object_name = 'latest_post_list'

	def get_queryset(self):
		return Post.objects.order_by('-pub_date')[:]

class DetailView(generic.DetailView):
	"""docstring for DetailView"""
	model = Post
	template_name = 'posts/detail.html'