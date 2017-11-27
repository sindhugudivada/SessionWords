from django.shortcuts import render, HttpResponse, redirect
from models import *
from datetime import datetime
from time import gmtime,strftime

# Create your views here.


def index(request):
    return render(request, 'session_words/index.html')

def getinfo(request):
    if request.method == "POST":
        if 'all_words' not in request.session:
            request.session['all_words']=[]
        else:
            request.session['all_words']=request.session['all_words']
        context={
        request.session['word'] : request.POST['word']
        request.session['color'] : request.POST['color']
        request.session['fonts'] : request.POST['fonts']
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S", gmtime())
        }
        request.session['all_words'].append(context)
        return redirect('/')
    else:
        return redirect('/')

def clear(request):   
    del request.session['word']
    return render(request,'/')
