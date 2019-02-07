from . import models
from django import forms
from django.forms import ModelChoiceField
from .models import movie,customer

class Movieform(forms.Form):
	name=forms.CharField(max_length=60,label='Movie Name')
	year=forms.IntegerField()
	genre_choice=(('AC','Action'),
				('TH','Thriller'),
				('CO','Comedy'),
				('RM','Romance'),
				('AD','Adventure'),
				('FC','Fiction'),
				('SF','Sci-Fi'))
	genre=forms.ChoiceField(choices=genre_choice)
	lang_choice=(('EN','English'),
				('SP','Spanish'),
				('FR','French'))
	lang=forms.ChoiceField(choices=lang_choice)
	rent_price=forms.DecimalField(max_digits=10, decimal_places=2)
	rented=forms.BooleanField(required=False)
	customer_name=forms.ModelChoiceField(queryset=customer.objects,required=False)


class UserCreate(forms.Form):
	username=forms.CharField(max_length=40,label='User Name')
	password=forms.CharField(widget=forms.PasswordInput())
	email = forms.EmailField()


class Userlogin(forms.Form):
	username=forms.CharField(max_length=40,label='User Name')
	password=forms.CharField(widget=forms.PasswordInput())
	