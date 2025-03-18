from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    id_photo = models.ImageField(upload_to='id_photos/', null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    id_photo = models.ImageField(upload_to='id_photos/')
    photo = models.ImageField(upload_to='profile_photos/')

    def __str__(self):
        return self.name

class CarRental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_registration = models.CharField(max_length=100,null=True)
    car_journey = models.CharField(max_length=100 , null=True)
    car_model = models.CharField(max_length=100,null=True)
    car_milege =  models.CharField(max_length=100,null=True)
    car_date = models.DateTimeField(auto_now_add=True)
    # amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    fuel_used = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.car_model} rented by {self.user.username}"

class CarReturn(models.Model):
    # rental = models.OneToOneField(CarRental, on_delete=models.CASCADE)
    return_date = models.DateTimeField(auto_now_add=True)
    car_picture = models.ImageField(upload_to='returned_cars/')
    condition = models.TextField()
    issues = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Return record for {self.rental.car_model}"