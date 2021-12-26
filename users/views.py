from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views as auth_views, authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import UserRegisterForm
from .models import Profile

@csrf_exempt
def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            Profile(user=user , national_id= user_form.cleaned_data['national_id'],type= user_form.cleaned_data['type']).save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        user_form = UserRegisterForm()
    return render(request, 'users/register.html', {'user_form': user_form})


@login_required
def profile(request):
    user = Profile.objects.filter(user=request.user)[0]
    return render(request, 'users/profile.html', {'national_id': user.national_id, 'type': user.type})

