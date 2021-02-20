from django import forms


class TablaForm(forms.Form):
    numero = forms.IntegerField()
