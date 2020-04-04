from django.shortcuts import render
#from models import *
from my_app.models import *



# Create your views here.
from django.http import HttpResponse
#def index(request):
	#return HttpResponse("Welcome!!!")

#settings /urls.py

def index(request):
	#return render(request,'index.html')
	s=Book.objects.all()
	#s = Books.objects.all()
	context = {"all_books":s,"name":"Sarmi"}
	return render(request,"index.html",context)
