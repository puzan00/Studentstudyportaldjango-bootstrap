from django import forms
from .models import Notes

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'cols': 30, 'rows': 5}),
        }