from django.shortcuts import render
from django.http import HttpResponse

def sum(request):
    a=5
    b=34
    s=a+b
    return HttpResponse(s)

# Create your views here.
