from django.shortcuts import render


# This file used for  Business logic

# Create your views here.


def post_list(request):
    return render(request, "app1/post_list.html", {})


def welcome(request):
    return render(request, "app1/welcome.html")