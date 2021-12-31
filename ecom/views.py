from django.shortcuts import render,HttpResponse
import mysql.connector
# Create your views here.

def home(request):
    try:
        pass
    except:
        pass
    return render(request,"index.html",)
