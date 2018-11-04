from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# We create our views here as methods, and when we create views in django we always pass an request argument.
def index(request):
    # return HttpResponse("Hey there.")
    return render (request, 'index.html',{})
    # Notice that render takes a request, the html file, and parameters. In this case is an empty dictionary but we can pass values as well. 

def post(request):
    return HttpResponse("I'm a single post page.")