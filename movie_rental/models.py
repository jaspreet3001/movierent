from django.db import models
from django.core.validators import RegexValidator
from django.forms import ModelForm
from django import forms





class customer(models.Model):

	name=models.CharField(max_length=40)
	#phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="enter in the format:'+999999999'")
	phone_number = models.CharField(max_length=10, blank=True) # validators should be a list
	email=models.EmailField(max_length=80,blank=True,null=True)
	address1=models.CharField(max_length=80,blank=True)
	address2=models.CharField(max_length=80,blank=True)
	age=models.IntegerField(default=0)

	def __str__(self):
		return self.name

class movie(models.Model):
	name=models.CharField(max_length=60)
	year=models.IntegerField()
	genre_choice=(('AC','Action'),
				('TH','Thriller'),
				('CO','Comedy'),
				('RM','Romance'),
				('AD','Adventure'),
				('FC','Fiction'),
				('SF','Sci-Fi'))
	genre=models.CharField(max_length=20,choices=genre_choice)
	lang_choice=(('EN','English'),
				('SP','Spanish'),
				('FR','French'))
	lang=models.CharField(max_length=12,choices=lang_choice)
	rent_price=models.DecimalField(max_digits=10, decimal_places=2,default=00.00)
	rented=models.BooleanField()
	customer_name=models.ForeignKey(customer,on_delete=models.SET_NULL, blank=True,null=True)

	def __str__(self):
		return self.name

class modelCustomer(ModelForm):
	class Meta:
		model=customer
		fields=['name', 'phone_number', 'email','address1','address2','age']


