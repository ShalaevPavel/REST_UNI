from django.shortcuts import render
from .models import String_Concatenation, String_Multiplication
from .forms import String_ConcatenationForm, String_MultiplicationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

"""
#Facade( пометил в коде)
По сути и есть фасад( дает клас из других классов), дающих абстракцию 
для прямого создания и сохранения объектов БД без создания самого объекта
Тесты к нему в файле test_forms.py
"""
def test(request):
    return HttpResponse("ok")

def index(request):
    if request.method == "POST":
        add_form = String_ConcatenationForm(request.POST, request.FILES)  # Facade
        if add_form.is_valid():
            add_form.save()

            return HttpResponseRedirect(reverse("index"))
        else:
            return HttpResponse("not valid")

    add_form = String_ConcatenationForm()
    new_ = String_Concatenation.objects.all().last()
    str3 = ""
    if new_ is not None:
        str3 = new_.string1 + new_.string2

    return render(request, "app/index.html", {"form": add_form, "result": str3})


def n_times_string(request):
    if request.method == "POST":
        mult_form = String_MultiplicationForm(request.POST, request.FILES)  # Facade
        if mult_form.is_valid():
            mult_form.save()

            return HttpResponseRedirect(reverse("multiply"))
        else:
            return HttpResponse("not valid")

    mult_form = String_MultiplicationForm()
    new_ = String_Multiplication.objects.all().last()

    str3 = ""
    if new_ is not None:
        str3 = new_.string_for_multiplication
        str3 *= new_.n

    return render(request, "app/mult.html", {"form_mult": mult_form, "result": str3})
