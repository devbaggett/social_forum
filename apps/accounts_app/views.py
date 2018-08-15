# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from . import forms


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    # reverse back to login page once they signedup
    success_url = reverse_lazy('login')
    template_name = 'accounts_app/signup.html'

