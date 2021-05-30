from django import forms



class LoginForm(forms.Form):
    username = forms.CharField(label='your name', max_length=20)
    password = forms.CharField(label='Your password', max_length=20)


class RegistrationForm(forms.Form):
    username = forms.CharField(label='your name', max_length=20)
    password = forms.CharField(label='Your password', max_length=20)