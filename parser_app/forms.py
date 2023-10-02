from django import forms
from . import models, parser

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('rezka.aq', 'rezka.aq'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class Meta:
        fields = [
            'media_type',
        ]


    def parser_data(self):
        if self.data['media_type'] == 'rezka.aq':
            rezka_parser = parser.parser()
            for i in rezka_parser:
                models.HdRezkaFilm.objects.create(**i)













