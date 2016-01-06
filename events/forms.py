from django import forms


class InformationForm(forms.Form):
    method = forms.CharField(label='Method', max_length=30)
    note = forms.CharField(label='Note', max_length=200)