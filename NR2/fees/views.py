from django.shortcuts import render
from django.http import HttpResponse

def user(request):
    # Get the 'name' parameter from the query string
    name = request.GET.get('name', 'Guest')  # Default to 'Guest' if 'name' is not provided
    return HttpResponse(f"Hello, {name}!")

def learnDJ(request):
    a="Django is very useful and popular framework of python"
    return HttpResponse(a)
# Create your views here.
