from django import forms
from operations.models import Mobile

class Formname(forms.Form):

    name=forms.CharField()
    email=forms.EmailField()
    about=forms.CharField(widget=forms.Textarea)

class EmiForm(forms.Form):
    loan_amount=forms.IntegerField()
    tenure=forms.IntegerField()
    Interest=forms.IntegerField()

class Register(forms.Form):
    name=forms.CharField()
    password1=forms.CharField()
    password2=forms.CharField()

class Book(forms.Form):
    title=forms.CharField()
    author= forms.CharField()
    publication=forms.CharField()

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = '__all__'
