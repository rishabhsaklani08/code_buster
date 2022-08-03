from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return(render(request, 'login/index.html'))


def signin(request):
    return(render(request, 'login/signin.html'))
    
def signup(request):
    return(render(request, 'login/signup.html'))
    
def signout(request):
    return(render(request, 'login/signout.html'))
    
