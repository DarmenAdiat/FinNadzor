# Generated by Django 5.0 on 2023-12-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinNadzor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialorganization',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='financialorganization',
            name='accountant',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Главный бухгалтер'),
        ),
    ]
