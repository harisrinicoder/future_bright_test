from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.


def blog_home(response):
    #return HttpResponse("Welcome to the Blog Home Page")
    return HttpResponse("<h1>Welcome to the Blog Home Page</h1>")


