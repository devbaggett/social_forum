from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

# connect posts to group
from ..groups.models import Group

# connect current post to whoever's logged in
from django.contrib.auth import get_user_model
User = get_user_model()

import misaka

# POSTS MODELS FILE
class Post(models.Model):
	user = models.ForeignKey(User, related_name='posts')
	created_at = models.DateTimeField(auto_now=True)
	message = models.TextField()
	message_html = models.TextField(editable=False)
	group = models.ForeignKey(Group, related_name='posts', null=True, blank=True)

	def __str__(self):
		return self.message

	def save(self,*args,**kwargs):
		self.message_html = misaka.html(self.message)
		super().save(*args,**kwargs)

	def get_absolute_url(self):
		return reverse('posts:single',kwargs={'username':self.user.username, 'pk':self.pk})

	class Meta:
		ordering = ['-created_at']
		# every message is uniquely linked to a user
		# unique_together = ['user', 'message']

