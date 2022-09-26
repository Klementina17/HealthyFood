from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):

    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}))
    password1 = forms.CharField(label="Password", max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm Password", max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    ages=[
        ('14-18', "14-18"),
        ('19-25', "19-25"),
        ('26-32',"26-32"),
        ('33+',"33+")]
    age = forms.CharField(widget=forms.RadioSelect(choices=ages))
    weight = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    height = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField( widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'age', 'weight', 'height', 'email']

# class breakfastPostForm(forms.ModelForm):
#
#     class Meta:
#         model = breakfastPost
#         exclude = ("user",)
