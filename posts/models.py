from django.db import models

# Create your models here.

class Post(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=64)
    contents=models.TextField()

    def __str__(self):
        return self.title