from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/homepage.html')

def dashboard(request):
    return render(request, 'home/profile/dashboard.html')
