from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Librarian(models.Model):
    student_number = models.PositiveBigIntegerField(primary_key=True)
    phone_number = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='librarian')
    def __str__(self) -> str:
        return f"{self.user.username} {self.user.last_name} {self.student_number}"

class Shift(models.Model):
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE, related_name='shifts')
    start_time = models.TimeField()
    end_time = models.TimeField()
    sat = 'Saturday'
    sun = 'Sunday'
    mon = 'Monday'
    tue = 'Tuesday'
    wed = 'Wednesday'
    thu = 'Thursday'
    fri = 'Friday'
    day_choices = (
        (sat, 'Saturday'),
        (sun, 'Sunday'),
        (mon, 'Monday'),
        (tue, 'Tuesday'),
        (wed, 'Wednesday'),
        (thu, 'Thursday'),
        (fri, 'Friday'),
    )
    day = models.CharField(max_length=9, choices = day_choices)