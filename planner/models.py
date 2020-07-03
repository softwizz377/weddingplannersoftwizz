from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import

# Create your models here.
class ContactUs(models.Model):
	
	firstname=models.CharField(max_length=200)
	lastname=models.CharField(max_length=200)
	phone=models.CharField(max_length=200, default='')
	city=models.CharField(max_length=200)
	subject=models.CharField(max_length=200,default='')
	class Meta:
		db_table="ContactUs"
	def __str__(self):
		return self.name
		
class Booking(models.Model):
	name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	date=models.CharField(max_length=200)
	time=models.CharField(max_length=200)
	Bookingfor=models.CharField(max_length=200)
	
	class Meta:
		db_table="booking"
	def __str__(self):
		return self.name
	
class Feedback(models.Model):
	name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	phone=models.CharField(max_length=200)
	message=models.CharField(max_length=200)
	
	
	class Meta:
		db_table="Feedback"
	def __str__(self):
		return self.name

class Gallery(models.Model):
	photo=models.ImageField(upload_to='images/')
	
	class Meta:
		db_table="Gallery"
	
class Vendorcategory(models.Model):
	title=models.CharField(max_length=200)
	photo=models.ImageField(upload_to='images/')
	class Meta:
		db_table="Vendorcategory"
	def __str__(self):
		return self.title
        
class Vendordetail(models.Model):
    name=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='images/')
    location=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    vcategory=models.ForeignKey(Vendorcategory,on_delete=models.CASCADE, default="")
    class Meta:
        db_table="Vendordetail"
    def __str__(self):
        return self.name  