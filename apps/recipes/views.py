from django.shortcuts import render

from django.http import HttpResponse

def view_home(request):
    return render(request,'recipes/home.html')

def view_contact(request):
    return HttpResponse("Contato")


def view_about(request):
    return HttpResponse("Sobre")


