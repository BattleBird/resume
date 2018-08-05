from django.urls import path
from . import views

app_name = 'interests'

urlpatterns = [
    path('', views.interests, name='interests')
]