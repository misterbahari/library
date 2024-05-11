from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymembers = Member.objects.get(id=id)
    template = loader.get_template('DETAILS.html')
    context = {
        'mymember': mymembers,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('MAIN.html')
    return HttpResponse(template.render())