from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Image,Profile
from django.contrib.auth.models import User


@login_required
def home(request):
    images = Image.objects.all()
    users = User.objects.all()
    return render(request, 'index.html',{"images":images, "users":users})


def get_search(request):
    
    if 'searchUser' in request.GET and request.GET["searchUser"]:
        search_word = request.GET.get("searchUser")
        searched_user = User.search_by_username(search_word)
        message = f"{search_word}"

        return render(request, 'index.html',{"message":message,"all_users": searched_user})

    else:
        message = "You haven't searched for anyone"
        return render(request, 'index.html',{"message":message})


