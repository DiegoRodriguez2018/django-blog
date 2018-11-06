from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.

# We create our views here as methods, and when we create views in django we always pass an request argument.
def index(request):
    #retriving all the posts instances:
    posts = Post.objects.all()
    # And rendering our view.
    return render (request, 'index.html',{'posts':posts})
    # Notice that we are passing parameters to our template in the dictionary. 

def post(request,slug):
    return render_to_response('post.html', {
        'post': get_object_or_404(Post,slug=slug) 
    })

def about(request):
    return render (request, 'about.html')
