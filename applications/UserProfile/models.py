from statistics import mode
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class UserInfo(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE)
    About = models.TextField()
    category = models.ForeignKey("category.Category",on_delete=models.CASCADE) 
    phone_number = models.CharField(max_length=10)
    address = models.TextField()
    gender = models.CharField(max_length=1,
    choices=(
        ('M',"Male"),
        ('F',"Female"),
    )
    )
    skill = models.ManyToManyField("skill.Skill")
    profile_pic = models.ImageField(upload_to="userprofil/")
    sccs = models.CharField(max_length=30)
    sschool_name = models.CharField(max_length=30)
    hsccs = models.CharField(max_length=30)
    hschool_name = models.CharField(max_length=30)
    dgree = models.CharField(max_length=30)
    college_name = models.CharField(max_length=30)


    def __str__(self):
        return self.About

