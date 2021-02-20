from django import forms

class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=35)
    contra = forms.CharField(label='Contraseña', widget=forms.PasswordInput)