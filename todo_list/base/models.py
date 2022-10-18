from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# this is how we creat our database


class Task(models.Model):
    # create some attributes make them and set them values
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
