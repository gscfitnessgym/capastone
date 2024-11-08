from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .models import Member





from django import forms
from .import models
from .models import Notification


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ('first_name', 'last_name', 'email_address', 'message')


class PredictionForm(forms.Form):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label="Gender")
    age = forms.IntegerField(min_value=1, max_value=100, initial=25, label="Age")
    height = forms.IntegerField(min_value=100, max_value=250, initial=170, label="Height (cm)")
    weight = forms.IntegerField(min_value=30, max_value=200, initial=70, label="Weight (kg)")
    duration = forms.IntegerField(min_value=1, max_value=180, initial=60, label="Duration (minutes)")
    heart_rate = forms.IntegerField(min_value=60, max_value=200, initial=100, label="Heart Rate")
    body_temp = forms.FloatField(min_value=35.0, max_value=43.0, initial=37.0, label="Body Temperature (°C)")

class MemberForm(forms.ModelForm):

     class Meta:
        model = Member
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'age',
            'address',
            'email_address',
            'gender',
            'phone_number',
            'pricing',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'middle_name': forms.TextInput(attrs={'placeholder': 'Middle Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address'}),
            'email_address': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'pricing': forms.NumberInput(attrs={'placeholder': 'Pricing'}),
        }