from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=60)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name