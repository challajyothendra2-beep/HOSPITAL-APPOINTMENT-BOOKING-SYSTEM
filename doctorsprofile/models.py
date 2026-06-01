from django.db import models
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    doctor = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    def __str__(self):
        return self.name