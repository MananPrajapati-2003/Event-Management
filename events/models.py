from django.db import models
from accounts.models import User

class Event(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=150)
    date = models.DateField(null=True) 
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class RSVP(models.Model):
    STATUS_CHOICES = [
        ('Going', 'Going'),
        ('Maybe', 'Maybe'),
        ('Not Going', 'Not Going')
    ]

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"


class Review(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.event.title} - {self.rating}"
