from django import forms

class MemeUploadForm(forms.Form):
    image = forms.ImageField()
    # Add other fields as needed for your form