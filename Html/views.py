from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Welcome to the User Module home Page")
def index(request):
    return render(request,'index.html')
# Create your views here.
