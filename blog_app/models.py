from django.db import models
from django.utils import timezone

# Create your models here.
class Blogdb(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.CharField(max_length=100,blank=True,null=True)
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateField(blank=True,null=True)

    def __str__(self):
        return self.title
