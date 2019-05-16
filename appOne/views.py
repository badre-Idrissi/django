from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

def hello(request):

    template = loader.get_template('appOne/index.html')
    return HttpResponse(template.render(), request)

def details(request):

    malist = [1,2,3]
    context = {
        "var1":malist,
        "var2":"value2"
    }
    ## recuperer les infos de la base de données et créer un context

    template = loader.get_template('appOne/details.html')
    return HttpResponse(template.render(context, request))

def pizzas(request, pizzaName):
    context = {
        "pizza":pizzaName.upper()
    }
    ## recuperer les infos de la base de données et créer un context

    template = loader.get_template('appOne/pizza.html')
    return HttpResponse(template.render(context, request))