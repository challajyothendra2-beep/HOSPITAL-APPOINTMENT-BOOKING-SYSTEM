from django.db import models
class appointmentbooking(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    def str (self):
        return self.name
        
    