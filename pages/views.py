from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request, 'pages/home.html')

def service_view(request):
    return render(request, 'pages/service.html')
