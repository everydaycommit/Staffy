from django import forms
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from .models import Employee,Request,Task,Meeting

class ActivityForm (forms.ModelForm):
    class Meta():
        model = Task
        fields = [
            'date',
            'time_start',
            'time_end',
            'is_remote',
            'descriptions'
        ]

class RegisterForm(ModelForm):
    class Meta():
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password'
        ]

class LoginForm(ModelForm):
    username = forms.CharField(
        max_length=200, min_length=4, required=True,label='نام کاربری',
        widget=forms.TextInput(
            attrs={ 'id':'username',
                    'class': 'form-control',
                    'placeholder': 'Paul_Anderson'}
        )
    )
    password = forms.CharField(
        max_length=200, min_length=4, required=True,label='رمز عبور',
        widget=forms.TextInput(
            attrs={ 'id':'password',
                    'class': 'form-control',
                    'type' : 'password',
                   'placeholder': '*123QWE@ewq*'}
        )
    )
    class Meta():
        model = User
        fields = [
            'username',
            'password'
        ]

class LeaveRequestForm (ModelForm):
    model = Request
    fields = [
        'employee',
        'title',
        'dayoff_from_date',
        'dayoff_to_date',
        'is_remote',
        'description',
        'created_at'
    ]