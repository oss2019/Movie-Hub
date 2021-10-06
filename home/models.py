from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    phonenumber=models.CharField(max_length=13)
    message=models.CharField(max_length=500)

    def __str__(self):
        return self.name