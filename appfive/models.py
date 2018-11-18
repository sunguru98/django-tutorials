from django.db import models
from django.contrib.auth.models import User
# User class already has email username password first name last name 
# Hence you just extend the functionality by adding a onetoonefield with the new model class
# Create your models here.

class UserProfileAndPortfolioInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    github_page = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to="profile_pictures", blank=True)

    def __str__(self):
        return self.user.username