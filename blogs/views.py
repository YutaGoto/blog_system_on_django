from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.template import loader
from django.views import generic
from django.urls import reverse
from django.utils import timezone

from .models import Post, Tag

class IndexView(generic.ListView):
    template_name = 'blogs/index.html'

    def get_queryset(self):
        return Post.objects.all[:5]

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blogs/detail.html'
