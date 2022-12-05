from django import forms
from .models import Document


class StudyFormClass(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )
