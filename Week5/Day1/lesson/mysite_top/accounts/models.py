from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#профиль пользователя
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
   
    def __str__(self):
        return f'Profile: {self.user.username}'
