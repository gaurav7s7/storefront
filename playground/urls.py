from django.urls import path
from . import views

# This is called a URLConf module
urlpatterns = [path('hello/', views.say_hello), path('helloh1/', views.say_hello_h1)]