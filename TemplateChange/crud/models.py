from django.db import models
# Create your models here.
class Tour(models.Model):
    upload = models.ImageField()
    price= models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.city

class Profile(models.Model):
    #Name, Date of birth, gender,phone number  and also
    #create user address model-with given fields owner=FK(Profile),
    #address1, address2, pincode
    GENDER_CHOICES = ( ('M', 'Homme'),('F', 'Femme'),)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    name = models.CharField(max_length=255)
    dob = models.DateField()
    def __str__(self):
        return self.name

class Address(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    address1 = models.TextField()
    address2 = models.TextField()
    pincode = models.CharField(("zip code"), max_length=5, default="43701")


    
