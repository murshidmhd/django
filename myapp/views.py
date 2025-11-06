from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Departments, Doctors
from .forms import BookingForm


def index(request):

    num1 = [1, 2, 3, 4, 5, 6, 7, 8]
    fruit = ["apple", "banana", "grapes"]
    numbers = {"num1": num1, "fruit": fruit}
    return render(request, "index.html", numbers)


def about(request):
    return render(request, "about.html")


def booking(request):

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("booking")
    else:
        form = BookingForm()

    return render(request, "booking.html", {"form": form})


def doctors(request):
    dict_docs = {"doctors": Doctors.objects.all()}
    return render(request, "doctors.html", dict_docs)


def contact(request):
    return render(request, "contact.html")


def department(request):
    dict_dept = {"dept": Departments.objects.all()}
    return render(request, "department.html", dict_dept)
