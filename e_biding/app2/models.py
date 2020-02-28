from django.db import models

class Admin(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=20)
    image=models.ImageField(upload_to='acc_image/')
    contact=models.IntegerField()
