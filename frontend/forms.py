from django import forms
from .models import Teachers

class TeachersForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Teachers