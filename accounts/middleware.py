# accounts/middleware.py

from django.shortcuts import redirect
from django.urls import reverse

class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        admin_path = reverse('admin:index')
        if request.path.startswith(admin_path):
            if not request.user.is_authenticated or not request.user.is_staff:
                return redirect('home')  

        response = self.get_response(request)
        return response
