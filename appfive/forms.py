from django import forms
from django.contrib.auth.models import User
from appfive.models import UserProfileAndPortfolioInfo
#Verify two things 
#1. delete line 7 and see
#2. replace line 16 as '__all__'
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileAndPortfolioForm(forms.ModelForm):
    class Meta():
        model = UserProfileAndPortfolioInfo
        fields = ('github_page','profile_picture')
