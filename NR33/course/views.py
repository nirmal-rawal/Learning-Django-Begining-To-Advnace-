from django.shortcuts import render

# Create your views here.
def Django(request):
    return render(request, 'course/courseinfo.html')