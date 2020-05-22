from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('accounts/profile/',views.UserProfile.as_view(),name="profile"),
    path('signup/', views.SignUpView.as_view(), name='signup'),

]