from django.db import models
class patient(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    def  str (self):
        return self.name