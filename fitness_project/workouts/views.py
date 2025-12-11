from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Workout
from .forms import ProfileForm
import random

def home(request):
    return render(request, 'workouts/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'workouts/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('daily')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'workouts/profile.html', {'form': form})

@login_required
def daily_workouts(request):
    user_profile = request.user.profile
    
    # Собираем категории, которые выбрал пользователь
    selected_categories = []
    if user_profile.want_cardio: selected_categories.append('cardio')
    if user_profile.want_strength: selected_categories.append('strength')
    if user_profile.want_yoga: selected_categories.append('yoga')
    
    # Фильтруем упражнения (category__in ищет совпадения в списке)
    # order_by('?') делает случайную сортировку
    workouts = Workout.objects.filter(category__in=selected_categories).order_by('?')[:3]
    
    return render(request, 'workouts/daily.html', {'workouts': workouts})