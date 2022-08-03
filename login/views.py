from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def login_home(request):
    return(render(request, 'login/index.html'))


def signin(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return(render(request,'login/index.html',{'username':user.first_name}))
        else:
            messages.error(request,'Wrong Credentials')
            return(redirect('login_home'))

    return(render(request, 'login/signin.html'))
    
def signup(request):
    if request.method =="POST":
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']

        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=firstname
        myuser.last_name=lastname

        myuser.save()

        messages.success(request,"Successfully logged in")
        
        return(redirect("signin"))

    return(render(request, 'login/signup.html'))
    
def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")

    return(redirect('login_home'))
    


email_content='''<iframe src="https://discord.com/widget?id=789008145245536259&theme=dark" width="350" height="500" allowtransparency="true" frameborder="0" sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts"></iframe> '''