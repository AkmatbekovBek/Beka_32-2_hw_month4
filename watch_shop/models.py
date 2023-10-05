from django.db import models
from django.contrib.auth.models import User


class watch(models.Model):

    WATCH_TYPE = (
        ('Мужские', 'Мужские'),
        ('Женские', 'Женские'),
        ('Унисекс','Унисекс'),
    )

    WATCH_BRANDS = (
        ('Apple Watch', 'Apple Watch'),
        ('Casio', 'Casio'),
        ('Rolex', 'Rolex'),
        ('Cartier', 'Cartier'),
        ('Seiko', 'Seiko'),
        ('Made in China', 'Made in China'),
    )

    title = models.CharField('Укажите название', max_length=70, null=True)
    description = models.TextField('Укажите описание наручных часов', null=True, blank=True)
    image = models.ImageField('Добавьте фото', upload_to='watch_photo/', null=True)
    watch_type = models.CharField('Часы', max_length=70, choices=WATCH_TYPE, null=True)
    watch_type2 = models.CharField('Бренд часов', max_length=70, choices=WATCH_BRANDS, null=True, blank=True)
    cost = models.PositiveIntegerField('Укажите цену', null=True)
    watch_location = models.CharField('Укажите местонахождение часов', max_length=70, null=True)
    watch_url = models.URLField('Укажите ссылку', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Часы'
        verbose_name_plural = 'Часы'



class Reviews(models.Model):
    review_stars = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )

    review_object = models.ForeignKey(watch, on_delete=models.CASCADE,
                                      related_name='comment_object')
    review_text = models.TextField('Напишите отзыв')
    review_stars = models.CharField(max_length=100, choices=review_stars)
    reviews_created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.review_text



class CustomUser(User):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


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


    user_type = models.IntegerField(choices=USER_TYPE, verbose_name="Выберите тип пользователя")
    phone_number = models.CharField('Номер телефона', max_length=17)
    Remeshok = models.CharField('Укажите цвет ремешка', max_length=77, null=True)
    postcode = models.CharField('Укажите почтовый индекс', max_length=22)
    country = models.CharField('Укажите Страну', max_length=77)
    location = models.CharField('Укажите Адрес', max_length=77)
    age = models.PositiveIntegerField('Укажите возраст', default=17)
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='Ваш пол')
    type_card = models.IntegerField(choices=TYPE_CARD, verbose_name='Тип карты', null=True)
    card_number = models.CharField('Номер карты', max_length=77)










