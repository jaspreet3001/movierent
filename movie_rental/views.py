from django.shortcuts import render,redirect,render_to_response	
from django.http import HttpResponse
from .models import customer,movie,modelCustomer
from .forms import Movieform, UserCreate, Userlogin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import MovieSerializer

# Create your views here.
def index(request):
	return render(request,'home.html',{})

def signup(request):

	if request.method == 'POST':
		form = UserCreate(request.POST)
		if form.is_valid():
			username=form.cleaned_data["username"]
			password= form.cleaned_data.get('password')
			email = form.cleaned_data["email"]
			user = User()
			user.username = username
			user.set_password(password)
			user.email = email
			user.save()
			return redirect('home')
	else:
		form = UserCreate()
	return render(request, 'signup.html', {'form': form})


def userlogout(request):
    logout(request)
    return redirect('home')

def userlogin(request):
	if request.method == 'POST':
		form= Userlogin(request.POST)
		print(request.POST)
		if form.is_valid():
			username=form.cleaned_data["username"]
			password= form.cleaned_data.get('password')
			print ("username is ", username)
			user= authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				return redirect('home')
			else:
				return HttpResponse("incorrect username or password")
	else:
		form= Userlogin()
	return render(request, 'login.html', {'form': form})

@login_required
def add_customer(request):
	if request.method=='POST':
		add_c=modelCustomer(request.POST)
		add_c.save()
		data=customer.objects.all()
	else:
		add_c=modelCustomer()
		return render(request, "add_cust.html", {"form": add_c})
	return render_to_response("customer.html",{'data':data})

def movies(request):
	movies_data=movie.objects.all()
	return render(request,'test4.html',{'movies_data':movies_data})

class movieslist(APIView):
	def get(self, request):
		movielist=movie.objects.all()
		serializer=MovieSerializer(movielist, many=True)
		return Response(serializer.data)



#HTTP response returns a table of movies


def available(request):
	movies_data=movie.objects.filter(customer_name= None)
	return render(request,'test5.html',{'movies_data':movies_data})


def assign(request):
	return HttpResponse('This is assign')

@login_required
def add_movie(request):
	if request.method=='POST':

		form1=Movieform(request.POST)
		#p=form1.save()
		# mdata=movie.objects.all()
		if form1.is_valid():
			name=form1.cleaned_data['name']
			year=form1.cleaned_data['year']
			genre=form1.cleaned_data['genre']
			year=form1.cleaned_data['year']
			rent_price=form1.cleaned_data['rent_price']
			lang=form1.cleaned_data['lang']
			rented=form1.cleaned_data['rented']
			customer_name=form1.cleaned_data['customer_name']
			print ('genre is ',genre)
			movieToSave=movie.objects.create(name=name,year=year,genre=genre,rent_price=rent_price,lang=lang,rented=rented, customer_name=customer_name)
			movieToSave.save()
			return redirect('movies')
	else:
		form1=Movieform()
	return render(request,'add_movie.html',{'form1':form1})
	 
	# return render_to_response("test4.html",{'mdata':mdata})
def rented(request):
	movies_data=movie.objects.exclude(customer_name= None)
	return render(request,'rented.html',{'movies_data':movies_data})

@login_required
def customers(request):
	mydata=customer.objects.all()
	return render(request,'customer.html',{'data': mydata})

@login_required
def delete_movie(request,m_num):
	movie.objects.get(id=m_num).delete()
	return redirect('movies')

@login_required
def delete_customer(request,c_num):
	customer.objects.get(id=c_num).delete()
	return redirect('customers')
