from django.shortcuts import render
from django.http import HttpResponse
from .models import area
def square(request):
	mydata=area.objects.all()
	return render(request,'shape.html',{'mydata':mydata})
	
# Create your views here.
 