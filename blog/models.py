from django.db import models
from django.conf import settings
# Create your models here.
from django.utils import timezone

# Hint: Any of the Django Model will be saved in DataBase

class Post(models.Model): # defining a Django Modle "Post" by using models.Model. 
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

