from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

def loginUser(request):
    
    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method == 'POST':
        # print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username = username)
        except:
            print("User not found")
            
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return redirect('profiles')
        else:
            print("Username or Password is incorrect")
    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def profiles(request):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id = pk)

    topskills = profile.skill_set.exclude(description__exact = "")
    otherskills = profile.skill_set.filter(description = "")

    context = {"profile": profile, 
               "topSkills": topskills, "otherSkills": otherskills}
    return render(request, 'users/user-profile.html', context)