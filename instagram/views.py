from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Image,Profile
from django.contrib.auth.models import User


@login_required
def home(request):
    images = Image.objects.all()
    users = User.objects.all()
    return render(request, 'index.html',{"images":images, "users":users})





