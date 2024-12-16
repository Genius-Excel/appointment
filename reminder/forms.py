from django import forms
from .models import ImageAds



class ImageAdsForm(forms.ModelForm):
    class Meta:
        model = ImageAds
        fields = ['image_url']