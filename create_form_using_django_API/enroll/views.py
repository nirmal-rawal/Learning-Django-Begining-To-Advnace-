from django.shortcuts import render
from.forms import StudentRegistrations

# Create your views here.
def showdata(request):
    fm= StudentRegistrations()
    return render(request, 'enroll/userrigestration.html',
{'form':fm})

