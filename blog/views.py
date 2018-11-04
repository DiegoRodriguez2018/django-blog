from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# We create our views here as methods, and when we create views in django we always pass an request argument.
def index(request):
    return HttpResponse("Hey there.")

def post(request):
    return HttpResponse("I'm a single post page.")