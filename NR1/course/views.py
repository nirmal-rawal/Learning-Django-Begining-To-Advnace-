from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_django(request):
    return HttpResponse("Hello Django")

def learn_python(request):
    return HttpResponse("<h1>learn python</h1>")

def learn_var(request):
    a='<h1>Hello variable</h1>'
    return HttpResponse(a)

def learn_math(request):
    a=10+4
    return HttpResponse(a)

def learn_format(requrst):
    a="NirmalRawal"
    return HttpResponse(f"Hello my name is {a}")