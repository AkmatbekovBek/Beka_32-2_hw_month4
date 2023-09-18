from django.db import models

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
    cost = models.PositiveIntegerField('Укажите цену', max_length=70, null=True)
    watch_location = models.CharField('Укажите местонахождение часов', max_length=70, null=True)
    watch_url = models.URLField('Укажите ссылку', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Часы'
        verbose_name_plural = 'Часы'

