from django.db import models
from django.contrib.auth.models import User
# Post
# СHOICES слева то что сохранится в базе данных, справа то что покажется пользователю
CATEGORY_CHOICES = (
    ('Dj', 'Django'),
    ('Js', 'Javascript'),
    ('C', 'C')
)

class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=3, choices = CATEGORY_CHOICES)
    publish_date = models.DateTimeField(auto_now_add=True) # когда создали
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True) #когда обновим 

    def __str__(self):
        return self.title
