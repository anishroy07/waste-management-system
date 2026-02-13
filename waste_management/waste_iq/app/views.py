import os
import openai
import json
from dotenv import load_dotenv

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages 
from django.conf import settings
from datetime import datetime



from django.contrib.auth.models import User 


def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def recycling_guide(request):
    return render(request, 'recycling_guide.html')


def Complaint_portal(request):
    if request.method == "POST":
       
        full_name = request.POST.get('full_name')
        mob_no = request.POST.get('mob_no')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        description = request.POST.get('description')
        image = request.FILES.get('image') 

        Complaint_portal = Complaint_portal(
            full_name=full_name, 
            mob_no=mob_no, 
            email=email, 
            subject=subject, 
            description=description, 
            image=image
        )
        # CRITICAL FIX: Use 'messages' module
        messages.success(request, "Complaint submitted successfully.")
         

    return render(request, 'complaint_portal.html')


def Driver_registration(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        mob_no = request.POST.get('mob_no')
        email = request.POST.get('email')
        address = request.POST.get('address')
        pin_code = request.POST.get('pin_code')
        ward_no = request.POST.get('ward_no')
        
        # CRITICAL FIX: Use the imported Model to create the object
        Driver_registration = Driver_registration(
            full_name=full_name, 
            mob_no=mob_no, 
            email=email, 
            address=address, 
            pin_code=pin_code, 
            ward_no=ward_no, 
           
            registration_date=datetime.now() 
        )
        messages.success(request, "Registration successful.")
        return redirect('driver_registration')

    return render(request, 'Driver_registration.html')


def Collected_waste(request):
    if request.method == "POST":
        dry_waste = request.POST.get('dry_waste')
        wet_waste = request.POST.get('wet_waste')
        plastic_waste = request.POST.get('plastic_waste')
        medical_waste = request.POST.get('medical_waste')
        e_waste = request.POST.get('E_waste') 
        remarks = request.POST.get('remarks')
        Collected_waste = Collected_waste(
            dry_waste=dry_waste, 
            wet_waste=wet_waste, 
            plastic_waste=plastic_waste, 
            medical_waste=medical_waste, 
            e_waste=e_waste, 
            remarks=remarks
        )
        messages.success(request, "Waste collection record saved.")
        return redirect('collected_waste')
        
    return render(request, 'collected_waste.html')

@login_required
def task(request):

    users = User.objects.all() 
    return render(request, 'task.html', {'users': users})



def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            messages.success(request, "Account created successfully!")
            return redirect('home')
        else:
            messages.error(request, "Signup failed. Please correct the errors below.")
            
    else:
        form = UserCreationForm()
        
    return render(request, 'signup.html', {'form': form})




load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

@csrf_exempt
def openai_chat(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")
        except (json.JSONDecodeError, KeyError):
            return JsonResponse({"error": "Invalid JSON or missing 'message'"}, status=400)

      
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for the WasteIQ waste management application. Provide accurate, helpful advice on recycling, waste segregation, and local regulations."},
                {"role": "user",  "content": user_message},
            ],
            temperature=0.7,
            max_tokens=150,
        )

       
        ai_reply = resp.choices[0].message.content.strip()

        return JsonResponse({"reply": ai_reply})

    return JsonResponse({"error": "Only POST allowed"}, status=405)