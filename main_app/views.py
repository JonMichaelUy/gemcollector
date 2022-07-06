from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
  # return HttpResponse('<h1>Homepage</h1>')
  return render(request, 'home.html')

def about(request):
  # return HttpResponse('<h1>About the gem collector</h1>')
  return render(request, 'about.html')