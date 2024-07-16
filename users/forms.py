from django import forms

from users.models import User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'patronymic', 'last_name', 'phone', 'email']


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    # class Meta:
    #     model = User
    #     fields = ['username', 'password']
