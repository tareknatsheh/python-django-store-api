from django.urls import path
from . import views #From current folder import the views module (module is like a class that has functions)

# This thing can't have a different name!
urlpatterns = [
    path('hello/', views.say_hello)
]