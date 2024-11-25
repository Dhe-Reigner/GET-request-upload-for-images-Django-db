from django.shortcuts import render
from .models import Showroom
from .models import Profile

# Create your views here.
def home(request):
    all_showrooms = Showroom.objects.all()
    return render(request, 'home.html',{
        'awesome':all_showrooms
    })

def attendees(request):
    all_profile = Profile.objects.all()
    return render(request, 'attendees.html',{
        'updates':all_profile
    })

def attendees_add(request):
    return render(request, 'attendees_add.html')
