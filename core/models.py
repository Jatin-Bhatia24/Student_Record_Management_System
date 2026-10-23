from django.db import models
from django.core.validators import RegexValidator


class Student(models.Model):
    name = models.CharField(max_length=60)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    phone = models.CharField(
        max_length=10,
        default='',
        validators=[RegexValidator(r'^\d{10}$', 'Enter a 10-digit phone number.')]
    )
    email = models.EmailField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name