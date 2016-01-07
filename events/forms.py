from django import forms


class InformationForm(forms.Form):
    method = forms.CharField(label='Method', max_length=30, required=False)
    note = forms.CharField(label='Note', max_length=200, required=False)