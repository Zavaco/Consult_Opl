from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return render(request,'Home_Page/index.html')

def base(request):
    return render(request, 'Home_Page/base.html')