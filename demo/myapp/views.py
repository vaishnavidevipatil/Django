from django.shortcuts import render, HttpResponse
from .models import TodoItem
import requests
# Create your views here.
# Routes for the application can be defined here.


def home(request):
    # return HttpResponse ('Hello World!')  # Render a simple template with a message
    return render(request,'home.html')  # Render the home.html template

def todos(request):
    items=TodoItem.objects.all()  # Fetch all TodoItem objects from the database
    return render(request, 'todos.html', {"todos":items })  # Render the todos.html template

