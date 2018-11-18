from django.shortcuts import render
from . import forms
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,"appfive/index.html")

def register(request):
    user_registered = False

    if request.method == "POST":
        user_form = forms.UserForm(request.POST)
        profile_form = forms.UserProfileAndPortfolioForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
            profile.save()

            user_registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileAndPortfolioForm()

    return render(request,'appfive/register.html',
                          {
                              'user_registered':user_registered,
                              'user_form':user_form,
                              'profile_form':profile_form
                           })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            
            else:
                return HttpResponse("Account is not active .. Please try with some other user ")
        else:
            print("Incorrect password recognised .. \n Username {} \n Password {} ".format(username,password))
            return HttpResponse("Incorrect Details Please try again !")
    
    else:
        return render(request,'appfive/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special_page(request):
    return HttpResponse("Logged in ... Check !!")