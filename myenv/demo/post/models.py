from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    post_date = models.DateField()

    def __str__(self):
        return self.name