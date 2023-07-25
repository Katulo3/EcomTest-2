from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    profile_pic = forms.ImageField(required=False, widget=forms.FileInput)

    class Meta:
        model = User

        fields = ["username", "first_name", "last_name", "email", "password1", "password2", "profile_pic"]


class EditUserForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    profile_pic = forms.ImageField(required=False, widget=forms.FileInput)

    class Meta:
        model = User

        fields = ["first_name", "last_name", "email", "password1", "password2", "profile_pic"]
