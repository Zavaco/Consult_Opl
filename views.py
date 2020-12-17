from django.shortcuts import render
from .models import Navbar
from django.http import HttpResponse

from .models import Navbar


def main(request):
    return render(request, 'Home_Page/index.html')


def base(request):
    menu = Navbar.objects.first()
    print(menu, "123123")
    context = {'menu': menu}
    return render(request, 'Home_Page/base.html', context)


def student(request):
    return render(request, 'Home_Page/student.html')


def student_list(request):
    data = Student.objects.all()
    return render(request, 'Home_Page/student.html', {"data": data})