from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Showroom(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    price = models.DecimalField(max_digits=10, default='', decimal_places=2)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.URLField()
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    # car_models = models.ManyToManyField('CarModel', related_name='showrooms')
    # car_brands = models.ManyToManyField('CarBrand', related_name='showrooms')
    # class Meta:
    #     verbose_name_plural = 'Showrooms'
    #     ordering = ['-created_at']
    
    def __str__(self):
        return self.name
    
class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # class Meta:
    #     verbose_name_plural = 'Profiles'
    #     ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    