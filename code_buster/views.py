from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    sign_in=''' <div class="sign_in">
    <a 
    href="login/" 
    class="mx-2"
    style="    
    display: flex;
    position: relative;
    margin: 15rem;
    padding-left: 128px;
    font-size: 52px;">
    Sign in</a>
</div>'''
    return HttpResponse(sign_in)