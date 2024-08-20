from django.shortcuts import render
from datetime import datetime

# Create your views here.

# def learn_django(request):
#     cname="Django"
#     duration="4 Months"
#     seats=12
#     django_details={'nm':cname,'dr':duration,'st':seats}
#     return render(request,"course/courseone.html",context=django_details)

# def learn_django(request):
#     django_details={'nm':"django is awesome"}
#     return render (request, "course/courseone.html",django_details)


def dt(request):
    d=datetime.now()
    return render(request,"course/courseone.html",{'dt':d})
