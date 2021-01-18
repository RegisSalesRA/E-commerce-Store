from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(
        max_length=250,
        help_text='eg. youremail@gmail.com')

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
            'email')


class ContactForm(forms.Form):
    subject = forms.Charfield(max_lenght=50,required=True)
    name = forms.Charfield(max_length=20, required=True)
    from_email = forms.EmailField(max_lengh=50,required=True)
    messege = forms.CharField(
        max_length = 500,
        widget = forms.Textarea(),
        help_text='Write here your messege!'
    )