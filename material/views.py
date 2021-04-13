from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,"admin-side/index.html")


# def pages(request):
    # return render(request,"admin-side/")