from django.shortcuts import render

# Create your views here.
def up(request):
    return render(request, "profile.html")
def bookings(request):
    return render(request, "appointmentbooking.html")
from django.shortcuts import render, redirect
from .models import Doctor, Appointment

def book_appointment(request):
    doctors = Doctor.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')

        doctor = Doctor.objects.get(id=doctor_id)
        Appointment.objects.create(
            name=name,
            phone=phone,
            email=email,
            doctor=doctor,
            date=date,
            time=time
        )

        return render(request, 'book.html', {
            'doctors': doctors,
            'success': True
        })

    return render(request, 'book.html', {'doctors': doctors})