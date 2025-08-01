from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in user right after signup
            return redirect('home')  # Or any page you want
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
