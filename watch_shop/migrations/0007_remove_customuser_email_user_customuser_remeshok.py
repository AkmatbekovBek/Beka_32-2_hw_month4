# Generated by Django 4.2.5 on 2023-10-05 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch_shop', '0006_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='email_user',
        ),
        migrations.AddField(
            model_name='customuser',
            name='Remeshok',
            field=models.CharField(max_length=77, null=True, verbose_name='Укажите цвет ремешка'),
        ),
    ]