from django import forms
from .models import SentimentModel

class SentimentForm(forms.ModelForm):
    Sentence = forms.CharField(max_length=5000, widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    ))
    class Meta:
        model = SentimentModel
        fields = [
            'Sentence'
        ]