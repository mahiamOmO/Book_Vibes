from django import forms
from .models import Ebook, Chapter


class EbookForm(forms.ModelForm):
    class Meta:
        model = Ebook
        fields = ['name', 'image', 'categories', 'summary']
        widgets = {
            'categories': forms.CheckboxSelectMultiple,
            'summary': forms.Textarea(attrs={'rows': 5}),
        }


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['title', 'content', 'order']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }
