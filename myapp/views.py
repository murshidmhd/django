from django.shortcuts import render


def cal():
    x = 1
    y = 2
    return x


def say_hello(request):
    context = {"user": "John"}
    return render(request, "myapp/hello.html", context)
