from django.forms import ModelForm
from django import forms
from .models import ImageModel


class ImageForm(ModelForm):
    image=forms.ImageField(widget=forms.FileInput(attrs={'class': 'upload-input'}))
    class Meta:
        model = ImageModel
        fields = ['image']
