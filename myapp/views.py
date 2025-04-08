from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Streak
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Add this with your other views
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirect to login page after signup
    template_name = 'registration/signup.html'  # Template we created earlier
    
@login_required
def streak_home(request):
    streak, created = Streak.objects.get_or_create(user=request.user)
    return render(request, 'streak/home.html', {'streak': streak})

@login_required
def update_streak(request):
    streak = Streak.objects.get(user=request.user)
    if streak.update_streak():
        messages.success(request, "Streak updated! Keep going!")
    else:
        messages.info(request, "You've already logged today's activity")
    return redirect('streak_home')