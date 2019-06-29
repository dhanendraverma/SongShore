from django.views import generic
from .models import Album
from django.views.generic.edit import  UpdateView, DeleteView, CreateView 
from django.urls import reverse_lazy  
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .form import UserForum
class IndexView(generic.ListView):
	template_name = 'music/index.html'
	context_object_name = 'all_albums'

	def get_queryset(self):
		return Album.objects.all()


class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/details.html'


class AlbumCreate(CreateView):
	model = Album
	fields = ['artist','album_title','genere','album_logo']

class AlbumUpdate(UpdateView):
	model = Album
	fields = ['artist','album_title','genere','album_logo']

class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy('music:index')