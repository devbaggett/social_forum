from __future__ import unicode_literals

from django.contrib import admin
from . import models

class PostInLine(admin.TabularInline):
	model = models.Post
	
class PostAdmin(admin.ModelAdmin):
	fields = ['user', 'message', 'message_html', 'group', 'created_at']
	search_fields = ['user', 'message']
	list_filter = ['user', 'message', 'group']
	list_display = ['user', 'message', 'created_at']



admin.site.register(models.Post)