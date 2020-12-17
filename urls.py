from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='home'),
    path('base/', views.base, name='base'),
    path('student', views.student_list, name='student')

]