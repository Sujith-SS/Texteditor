from django import forms

class TextEditorForm(forms.Form):
    font_family = forms.CharField(max_length=250)
    font_size = forms.CharField(max_length=250)
    editor = forms.CharField(widget=forms.Textarea)

