from django.shortcuts import render
from django.contrib import messages

# Create your views here.


def index(request):
    messages.info(request, "Welcome to Dotshirt!")
    messages.success(request, "Enjoy your stay.")
    return render(request, 'home/index.html')