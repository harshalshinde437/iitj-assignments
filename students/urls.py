from django.urls import path
from .views import student_list, student_create

urlpatterns = [
    path('', student_list, name='student_list'),
    path('create/', student_create, name='student_create'),
]
