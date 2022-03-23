from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE)
    About = models.TextField()
    Company_logo = models.ImageField(upload_to="companyLogo")
    category = models.ForeignKey("category.Category",on_delete=models.CASCADE) 
    phone_number = models.CharField(max_length=10)
    address = models.TextField()
    gender = models.CharField(max_length=1,
    choices=(
        ('M',"Male"),
        ('F',"Female"),
    )
    )
    skill = models.ForeignKey("skill.Skill",on_delete=models.CASCADE)
    