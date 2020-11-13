from django.shortcuts import render

def index(request):
    return render(request, 'StuDash/index.html')

# Create your views here.
