

# Create your views here.
from django.shortcuts import render

# Create your views here.

def list(request):
	return render(request, 'frontend/list.html')