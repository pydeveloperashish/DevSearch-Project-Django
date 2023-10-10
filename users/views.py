from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import Profile


# Create your views here.

def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method == 'POST':
        # print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, "User not found")
            
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "Username or Password is incorrect")
    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.info(request, "User was successfully logged out")
    return redirect('login')


def registerUser(request):
    page = 'register'
    # form = UserCreationForm()
    form = CustomUserCreationForm()
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User was successfully registered...")
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "An error has occurred while registering...")
        
    context = {"page" : page, "form" : form}
    return render(request, 'users/login_register.html', context)


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


@login_required(login_url = 'login')
def userAccount(request):
    # Get the user profile
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    
    context = {"profile": profile, 
               "skills": skills,
               'projects': projects}
    return render(request, 'users/account.html', context)