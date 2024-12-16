from django import forms
from .models import ImageAds



class ImageAdsForm(forms.ModelForm):
    class Meta:
        model = ImageAds
        fields = ['image_url']

        widgets = {
            'image_url': forms.TextInput(attrs={'placeholder': 'Enter Image URL'})
        }

    def __init__(self, *args, **kwargs):
        super(ImageAdsForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'id': 'imageUrl'})
