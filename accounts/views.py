import json
from django.shortcuts import render
import google.generativeai as genai
import os

# Configure the generati've AI client
genai.configure(api_key="AIzaSyDZ125y0vyB0-G_nZut3jQNjLO0HPP9v4s")

# Create your views here.
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect('home')  # Redirect to a home page or dashboard
    #     else:
    #         messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def register_view(request):
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     user = User.objects.create_user(username=username, email=email, password=password)
    #     messages.success(request, 'Account created successfully')
    #     return redirect('login')
    return render(request, 'registration.html')

def about_view(request):
    return render(request, 'about.html')
def thrill(request):
    return render(request, 'thrill.html')
def cultural(request):
    return render(request, 'cultural.html')
def nature(request):
    return render(request, 'nature.html')
def romantic(request):
    return render(request, 'romantic.html')
def about_us(request):
    return render(request, 'about_us.html')
def contact_us(request):
    return render(request, 'contact_us.html')
def Tindia(request):
    return render(request, 'Tindia.html')
def Tnz(request):
    return render(request, 'Tnz.html')
def Tsa(request):
    return render(request, 'Tsa.html')
def Taus(request):
    return render(request, 'Taus.html')
def Tcr(request):
    return render(request, 'Tcr.html')
def Tnepal(request):
    return render(request, 'Tnepal.html')

def create_itinerary(request):
    itinerary = None
    if request.method == 'POST':
        destination = request.POST.get('destination')
        days = request.POST.get('days')

        # Create a prompt for the generative model
        prompt = f"Create a {days}-day itinerary for a trip to {destination}. give only json response  nothing else start from curly bracket only in  formst title description days inside days title activaities"

        try:
            # Use the generative model to generate the itinerary
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            itinerary = json.loads(response.text)
            print(itinerary)
        except Exception as e:
            itinerary = f"An error occurred: {str(e)}"

    # Ensure the path is correct relative to your templates directory
    return render(request, 'thrill.html', {'itinerary': itinerary})
