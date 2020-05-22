from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class UserProfile(TemplateView):
    template_name = 'dashboard/profile.html'