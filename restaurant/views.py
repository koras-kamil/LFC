

# Create your views here.
from django.shortcuts import render
from django.utils import timezone
from .models import Food ,SingletonModel , Shake , Salat

def index(request):
    # Count of orders placed today
   

    # List of available food items
    available_food = Food.objects.all()
    shakes=Shake.objects.all()
    singleton = SingletonModel.objects.first()
    salat=Salat.objects.all()

    context = {
        'singleton' : singleton,
        'available_food': available_food,
        'shakes': shakes,
        'salat': salat
    }
    return render(request, 'index.html', context)
