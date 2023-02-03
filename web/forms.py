from django import forms
from account.models import User
class edit_info_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('fullname', 'file_number', 'password')
        widgets = {
            'fullname':forms.TextInput(attrs={'class':'input100', 'placeholder': 'نام کامل بیمار'}),
            'filo_number':forms.TextInput(attrs={'class':'input100', 'placeholder': 'ماره پرونده'}),
            'password': forms.PasswordInput(attrs={'class':'input100', 'placeholder': 'گذرواژه'}),
        }

