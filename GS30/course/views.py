from django.shortcuts import render


# Create your views here.
def leran_django(request):
    return render(request,"course/info.html",{'nm':'Django course'})