from django.db import models

# Create your models here.
Users_CHOICES = (
   ('P', 'Patient'),
   ('D', 'Doctor')
)

class Profile(models.Model):
    user = models.CharField(choices=Users_CHOICES, max_length=128)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254,primary_key=True)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
