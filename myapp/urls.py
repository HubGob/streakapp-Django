from django.urls import path
from .views import streak_home, update_streak , SignUpView

urlpatterns = [
    path('', streak_home, name='streak_home'),
    path('update-streak/', update_streak, name='update_streak'),
    path('signup/', SignUpView.as_view(), name='signup'),
]