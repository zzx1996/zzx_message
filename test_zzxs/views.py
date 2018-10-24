from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Post

class Index(ListView):
    model = Post
    template_name = 'test_zzxs/index.html'
    ordering = ['-date']

class Write(CreateView):
    model = Post
    template_name = 'test_zzxs/write.html'
    fields = ['text','name']
    success_url = reverse_lazy('index')

# Create your views here.
