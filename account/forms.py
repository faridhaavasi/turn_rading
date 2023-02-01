from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from account.models import User
from django.core import validators
class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = '__all__'


class Login_Form(forms.Form):
    phone = forms.CharField(
        widget=forms.TextInput(
        attrs={'type':'text','placeholder':'شماره همراه'}
    ))
    password = forms.CharField(
        widget=forms.TextInput(
         attrs={'type':'password','placeholder':'پسورد'}
    ))

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone[0:1] != '09':
            raise ValidationError('ماره حتما باید تلفن همراه باشد','invalid lrn phone_number')
        if len(phone) > 11:
            raise ValidationError('ماره تلفن صحیح نیست','invalid phone_number')
        return phone

class Registerform(forms.Form):
     phone = forms.CharField(
        widget=forms.TextInput(
        attrs={'type':'text','placeholder':'شماره همراه'}
    ))
     
    