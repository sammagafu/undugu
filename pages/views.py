from django.shortcuts import render
from django.urls import reverse_lazy
from . forms import SignUpForm
from django.views.generic import TemplateView,CreateView
# Create your views here.

class UserProfile(TemplateView):
    template_name = 'dashboard/profile.html'


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'