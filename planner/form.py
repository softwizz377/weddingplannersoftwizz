from django import forms
from planner.models import ContactUs,Booking, Feedback
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ContactUsform(forms.ModelForm):
	firstname=forms.CharField(max_length=200)
	lastname=forms.CharField(max_length=200)
	phone=forms.CharField(max_length=200)
	city=forms.CharField(max_length=200)
	subject=forms.CharField(max_length=200)
	
	class Meta:
		model=ContactUs
		fields="__all__"
		
class Bookingform(forms.ModelForm):
	name=forms.CharField(max_length=200)
	email=forms.CharField(max_length=200)
	date=forms.CharField(max_length=200)
	time=forms.CharField(max_length=200)
	Bookingfor=forms.CharField(max_length=200)

	
	class Meta:
		model=Booking
		fields="__all__"
		
class Feedbackform(forms.ModelForm):
	name=forms.CharField(max_length=200)
	email=forms.CharField(max_length=200)
	phone=forms.CharField(max_length=200)
	message=forms.CharField(max_length=200)
	

	
	class Meta:
		model=Feedback
		fields="__all__"		