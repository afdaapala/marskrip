from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
	return render(request ,'index.html')

def otomatis(request):
	return HttpResponse("<h1>mantips</h1>")

def sdn(request):
	return HttpResponse("<h1>mantips</h1>")