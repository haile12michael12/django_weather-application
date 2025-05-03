
from django import forms

class WordForm(forms.Form):
    word = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter a word...'
    }))
