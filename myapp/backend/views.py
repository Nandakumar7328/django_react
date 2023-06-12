from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.

def save_user_details(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        password = make_password(data.get('password'))
        user_details = create_account(name=name,email=email,password=password)
        user_details.save()
        return JsonResponse({"res":"sucesss"})
    else:
        return JsonResponse({"res":"Hello React"})
    
