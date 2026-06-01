from django.shortcuts import render
from .models import appointmentbooking
def time(request):
    return render(request, 'time.html')
def book(request):
    return render(request,'book.html')
def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def profile(request):
    return render(request,'doctorsprofiles.html')
def register(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone=request.POST.get('phone')
        register.objects.create(
            username=username,
            password=password,
            email=email,
        )
    return render(request, 'register.html')
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import appointmentbooking
from rest_framework import status
from .serializers import AppointmentbookingSerializers
@api_view(['GET'])
def get_appointmentbooking(request):
    return Response(AppointmentbookingSerializers({'name':"challa","age":23}))
