from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def odd_even(request):
    a=45
    if a%2==0:
        return HttpResponse(f"this number{a} is even")
    else:
        return HttpResponse(f"the number {a} is odd")