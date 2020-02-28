from django.db import models

class User(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    pasw=models.CharField(max_length=50)
    contact=models.IntegerField(unique=True)
    date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=10)
    id=models.AutoField(primary_key=True)
    image=models.ImageField(upload_to='user_image/')

    def __str__(self):
        return self.id

class Product(models.Model):
    p_id=models.AutoField(primary_key=True)
    p_name=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    p_status=models.CharField(max_length=20)
    bid_price=models.IntegerField()
    dics=models.TextField(max_length=300)
    img=models.ImageField(upload_to='products/')
    user=models.ForeignKey(User,on_delete=models.CASCADE)


class Biding(models.Model):
    bidid=models.AutoField(primary_key=True)
    pid=models.ForeignKey(Product,on_delete=models.CASCADE)
    uid=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.FloatField()
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)

class Maxamout(models.Model):
    maid=models.AutoField(primary_key=True)
    pid=models.ForeignKey(Product,on_delete=models.CASCADE)
    uid=models.ForeignKey(User,on_delete=models.CASCADE)
    maxamount=models.FloatField()
