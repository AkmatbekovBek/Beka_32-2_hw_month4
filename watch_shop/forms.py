from django import forms
from . import models

class WatchShopForm(forms.ModelForm):
    class Meta:
        model = models.watch
        fields = '__all__'