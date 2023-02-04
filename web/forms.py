from django import forms
from account.models import User
class edit_info_form(forms.Form):
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'type': 'text', 'placeholder': 'شماره همراه'}
        ))
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={'type': 'text', 'placeholder': 'نام کامل بیمار'}
        ))
    file_number = forms.CharField(
        widget=forms.TextInput(
            attrs={'type': 'text', 'placeholder': 'شماره پرونده بیمار'}
        ))
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={'type': 'text', 'placeholder': 'یک گذرواژه وارد کنید'}
        ))




