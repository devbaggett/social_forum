# POSTS VIEWS

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.http import Http404

# pip insall django-braces
from braces.views import SelectRelatedMixin

from . import models
from . import forms

from django.contrib.auth import get_user_model
User = get_user_model()


class PostList(SelectRelatedMixin, generic.ListView):
	model = models.Post
	# mixin for the foreign keys of this post
	select_related = ('user', 'group')


class UserPosts(generic.ListView):
	model = models.Post
	template_name = 'posts/user_post_list.html'

	def get_queryset(self):
		# try to set user equal to whatever user is logged in and fetch posts related to user.
		try:
			self.post.user = User.objects.prefect_related('posts').get(username__iexact=self.kwargs.get('username'))
		# user got deleted
		except User.DoesNotExist:
			raise Http404
		else:
			return self.post_user.posts.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['post_user'] = self.post_user
		return context


class PostDetail(SelectRelatedMixin, gener.DetailView):
	model = models.Post
	select_related = ('user', 'group')

	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.filter(user__username__iexact=self.kwargs.get('username'))


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
	fields = ('message', 'group')
	model = models.Post

	# connect posts to user itself
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return super().form_valid(form)


class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
	model = models.Post
	select_related = ('user', 'group')
	# confirm url leads back to all posts
	success_url = reverse_lazy('posts:all')

	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.filter(user_id = self.request.user.id)

	def delete(self,*args,**kwargs):
		messages.success(self.request, 'Post Deleted')
		return super().delete(*args,**kwargs)
