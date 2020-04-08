from django.db import models
from datetime import datetime
# Create your models here.
class Service(models.Model):

    s_name = models.CharField(max_length=150)
    s_content = models.TextField()
    s_photo = models.ImageField(upload_to='Service/%Y/%m/%d/', blank=True)

    def __str__(self):
         return self.s_name

class Portfolio(models.Model):

    project_name = models.CharField(max_length=200)
    p_title = models.CharField(max_length=200)
    p_subtitle = models.CharField(max_length=200)
    p_photo = models.ImageField(upload_to='portfolio/%Y/%m/%d/', blank=True)
    p_conent = models.TextField(blank=True)
    used_technology = models.TextField(blank=True)
    p_client = models.CharField(max_length=200)
    p_category = models.CharField(max_length=200)
    p_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.project_name

class About(models.Model):

    a_title = models.CharField(max_length=141)
    a_photo = models.ImageField(upload_to='About/%Y/%m/%d/', blank=True)
    a_date = models.DateTimeField(default=datetime.now, blank=True)
    a_content = models.TextField()

    def __str__(self):
        return self.a_title

class Team(models.Model):
   member_name = models.CharField(max_length=155)
   member_photo = models.ImageField(upload_to='Team/%Y/%m/%d/', blank=True)
   member_deg = models.CharField(max_length=50)
   twitter = models.CharField(max_length=152)
   fb = models.CharField(max_length=150)
   linkedin = models.CharField(max_length=151)

   def __str__(self):
       return self.member_name

class Contact(models.Model):
    c_name = models.CharField(max_length=155)
    c_email = models.EmailField()
    c_phone = models.CharField(max_length=150)
    c_message = models.TextField()

    def __str__(self):
        return self.c_name