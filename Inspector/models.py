from django.db import models
import random

# Create your models here.

STATE_CHOICES =  (('AndhraPradesh','AndhraPradhesh'), ('Assam','Assam'), ('ArunachalPradesh','ArunanchalPradesh'), ('Bihar','Bihar'), ('Goa','Goa'), ('Gujarat','Gujrat'), ('JammuKashmir','JammuKashmir'), ('Jharkhand','JharKhand'), ('WestBengal','WestBengal'), ('Karnataka','Karnataka'), ('Kerala','Kerala'), ('MadhyaPradesh','MadhyaPradesh'), ('Maharashtra','Maharashtra'), ('Manipur','Manipur'), ('Meghalaya','Meghalaya'), ('Mizoram','Mizoram'), ('Nagaland','Nagaland'), ('Orissa','Orissa'), ('Punjab','Punjab'), ('Rajasthan','Rajasthan'), ('Sikkim','Sikkim'), ('TamilNadu','TamilNadu'), ('Tripura','Tripura'), ('UttaraKhand','UttaraKhand'), ('UttarPradesh','UttarPradesh'), ('Haryana','Haryana'), ('HimachalPradesh','HimachalPradesh'),('Chhattisgarh','Chattishgarh'))

class Fir(models.Model):
    Name = models.CharField(max_length=122,null=True,blank=True)
    Address = models.CharField(max_length=122,null=True,blank=True)
    City = models.CharField(max_length=122,null=True,blank=True)
    State = models.CharField(max_length=122,choices=STATE_CHOICES,default='MAHARASHTRA')
    Pincode = models.CharField(max_length=122,null=True,blank=True)
    Addhar =models.CharField(max_length=122,null=True,blank=True)
    Img = models.ImageField(upload_to='images/')
    Firdescription = models.TextField(null=True,blank=True)
    Date = models.DateField(null=True,blank=True)
    Time = models.TimeField(null=True,blank=True)
    Status = models.CharField(max_length=122,default='Action Pending')
    objects = models.Manager()

    def __str__(self):
        return self.Name

class Contact(models.Model):
    name = models.CharField(max_length=122,null=True,)
    email = models.CharField(max_length=122,null=True,)
    phoneno = models.CharField(max_length=10,null=True,)
    Report = models.CharField(max_length=122,null=True,)
    objects = models.Manager()

    def __str__(self):
        return self.name

class StatusDetails(models.Model):
    Name = models.CharField(max_length=122,null=True,blank=True)
    Addhar = models.CharField(max_length=122,null=True,blank=True)

    def __str__(self):
        return self.Name
        