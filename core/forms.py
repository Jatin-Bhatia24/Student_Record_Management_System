from django import forms
from .models import Student


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("name", "roll", "city", "phone", "email")

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student name'}),
            'roll': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter roll number'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter 10-digit phone number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email (optional)'}),
        }