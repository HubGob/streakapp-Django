from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Streak(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_streak = models.PositiveIntegerField(default=0)
    longest_streak = models.PositiveIntegerField(default=0)
    last_activity_date = models.DateField(auto_now_add=True)
    
    def update_streak(self):
        today = timezone.now().date()
        
        # If already logged in today, do nothing
        if self.last_activity_date == today:
            return False
            
        yesterday = today - timezone.timedelta(days=1)
        
        # If logged in yesterday, increase streak
        if self.last_activity_date == yesterday:
            self.current_streak += 1
        else:
            # Otherwise reset streak
            self.current_streak = 1
            
        # Update longest streak if needed
        if self.current_streak > self.longest_streak:
            self.longest_streak = self.current_streak
            
        self.last_activity_date = today
        self.save()
        return True