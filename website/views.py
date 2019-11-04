from django.shortcuts import render

def home(request):
	return render(request, 'website/home.html')

def services(request):
	return render(request, 'website/services.html')