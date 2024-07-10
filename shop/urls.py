from django.urls import path
from . import views #to avoid ambiguity of multiple voew files

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>', views.single_course, name="single_course")
]
