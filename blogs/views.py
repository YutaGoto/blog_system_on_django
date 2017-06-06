from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.template import loader
from django.views import generic
from django.urls import reverse
from django.utils import timezone

from .models import Post, Tag, PostsTag

class IndexView(generic.ListView):
    template_name = 'blogs/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Post.objects.all()

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blogs/detail.html'

    def get_queryset(self):
        return Post.objects.filter()
