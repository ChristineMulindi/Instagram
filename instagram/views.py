from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Image,Profile
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProfileForm


@login_required
def home(request):
    images = Image.objects.all()
    users = User.objects.all()
    return render(request, 'index.html',{"images":images, "users":users})


def get_search(request):
    
    if 'searchUser' in request.GET and request.GET["searchUser"]:
        search_word = request.GET.get("searchUser")
        searched_user = Profile.search_by_username(search_word)
        message = f"{search_word}"

        return render(request, 'index.html',{"message":message,"all_users": searched_user})

    else:
        message = "You haven't searched for anyone"
        return render(request, 'search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def profile(request, id):
    user = User.objects.get(id=id)
    current_user = request.user
    images = Image.objects.filter(user_profile_id = id)

    try:
        profile = Profile.objects.get(user_id=id)
    except ObjectDoesNotExist:
        return redirect(update_profile, current_user.id)   
    else:
        return render(request, 'profile.html',{"user":user, "images":images, "profile":profile})


@login_required(login_url='/accounts/login/')
def update_profile(request,id):
    current_user = request.user
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user_id =id
            profile.save()
        return redirect(home)

    else:
        form = ProfileForm()
    return render(request, 'update_profile.html', {"user": user, "form": form})  