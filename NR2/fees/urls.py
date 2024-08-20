from.import views
from django.urls import path

urlpatterns=[
    path("django/",views.learnDJ),
    path("user/",views.user)
]