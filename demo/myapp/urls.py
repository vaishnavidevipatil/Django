from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home route
    path("todos/", views.todos, name='todos'),  # Route for todo items

]
