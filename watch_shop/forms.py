from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm

class WatchShopForm(forms.ModelForm):
    class Meta:
        model = models.watch
        fields = '__all__'


class WatchShopReviewsForm(forms.ModelForm):
    class Meta:
        model = models.watch
        fields = '__all__'


ADMIN = 1
VIPClient = 2
CLIENT = 3

USER_TYPE = (
    (ADMIN, 'Администратор'),
    (VIPClient, 'VIP Клиент'),
    (CLIENT, 'Клиент')
)


MALE = 1
FEMALE = 2

GENDER_TYPE = (
    (MALE, 'М'),
    (FEMALE, 'Ж')
)


MBANK = 1
QIWI = 2
MASTERCARD = 3
PAYPAL = 4
VISA = 5
MAESTRO = 6
BTБ = 7

TYPE_CARD = (
        (MBANK, 'MBANK'),
        (QIWI, 'QIWI'),
        (MASTERCARD, 'MASTERCARD'),
        (PAYPAL, 'PAYPAL'),
        (VISA, 'VISA'),
        (MAESTRO, 'MAESTRO'),
        (BTБ, 'BTБ'),
)

class RegistraionNewForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    type_card = forms.ChoiceField(choices=TYPE_CARD, required=True)
    country = forms.CharField(required=True)
    location = forms.CharField(required=True)
    card_number = forms.CharField(required=True)
    postcode = forms.CharField(required=True)
    Remeshok = forms.CharField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'user_type',
            'gender',
        )

    def save(self, commit=True):
        user = super(RegistraionNewForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user