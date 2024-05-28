from django import forms

class SimpleForm(forms.Form):
    login = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)