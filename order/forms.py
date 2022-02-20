from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.forms import PasswordInput, TextInput
from order.models import UserDetail


class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username','password','email']
        widgets={
            'name': TextInput(

            ) ,
            'password':PasswordInput(attrs={
            'placeholder':'super secret',
            'class':'form-control'
        })}


    def save(self,commit= True):
        instance = super().save(commit=False)

        instance.name = self.cleaned_data.get('username').lower()

        if commit:
            instance.save()

        return instance

class UserDetail(forms.ModelForm):
    class Meta:
        model=UserDetail
        fields ='__all__'
