from django.shortcuts import render

# Create your views here.
def learn_python(request):
    return render(request,'fees/feesone.html',{'title':"learnpython","cname":" learn full course python"})