from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('accounts/profile/',views.UserProfile.as_view(),name="profile")
]