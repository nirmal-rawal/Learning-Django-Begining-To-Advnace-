from django.urls import path
from .import views

urlpatterns=[
    path('num/',views.num),
    path('numpy/',views.num)
]