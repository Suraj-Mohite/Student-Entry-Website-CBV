from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mob_number=models.IntegerField()
    image=models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.name