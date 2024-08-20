from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def max(request):
    a=23
    b=21
    if a>b:
        return HttpResponse(f"{a} is grater then {b}")
    elif a==b:
        return HttpResponse(f"{a} is equal to {b}")
    
    else:
        return HttpResponse(f"{b} is greater then {a}")

