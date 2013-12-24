# Create your views here.
from django.shortcuts import render

def home(request):
	template = 'index.html'
	return render(request,template,locals())# Create your views here.
