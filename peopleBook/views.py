from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from peopleBook.people import people as people_

from peopleBook.models import People


def details(request, name):
    user = people_[name]
    context = {
        'user':user
    }
    template = loader.get_template("peopleBook/details.html")
    return HttpResponse(template.render(context, request))

def people(request):
    users = People.objects.all()

    context = {
        'users':users
    }
    template = loader.get_template("peopleBook/people.html")
    return HttpResponse(template.render(context, request))


# Create your views here.
