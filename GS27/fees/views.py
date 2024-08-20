from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def num(request):
    return render(request,"fees/feesone.html")

def numr(request):
    return HttpResponse(request,"fees/feestwo.html")


