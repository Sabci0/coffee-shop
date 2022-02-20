from django import forms
from django.contrib.auth.hashers import make_password
from django.forms import PasswordInput, TextInput

from order.models import User





class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','password']
        widgets={
            'name': TextInput(

            ) ,
            'password':PasswordInput(attrs={
            'placeholder':'super secret',
            'class':'form-control'
        })}


    def save(self,commit= True):
        instance = super().save(commit=False)
        instance.password = make_password(self.cleaned_data.get('password'))
        instance.name = self.cleaned_data.get('name').lower()

        if commit:
            instance.save()

        return instance
