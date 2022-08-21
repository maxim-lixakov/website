from django.db import models


class User(models.Model):
    login = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=10)
    reg_date = models.DateField(auto_now=True)
    name = models.CharField(max_length=20)


class User_data(models.Model):
    year = models.IntegerField()
    month = models.CharField(max_length=20)
    day = models.IntegerField()
    text = models.TextField()
    login = models.ForeignKey(User, on_delete=models.CASCADE)