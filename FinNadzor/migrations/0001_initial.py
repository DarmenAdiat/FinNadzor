# Generated by Django 5.0 on 2023-12-12 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Executive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='ФИО')),
                ('iin', models.CharField(blank=True, default='000000000000', max_length=15, null=True, verbose_name='ИИН')),
                ('position', models.CharField(blank=True, max_length=250, null=True, verbose_name='Должность')),
                ('contacts', models.CharField(blank=True, max_length=250, null=True, verbose_name='Контактная информация')),
            ],
            options={
                'verbose_name': 'Руководители',
                'verbose_name_plural': 'Руководители',
            },
        ),
        migrations.CreateModel(
            name='FinancialOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Полное наименование')),
                ('chairman', models.CharField(blank=True, max_length=250, null=True, verbose_name='Председатель')),
                ('email', models.EmailField(blank=True, default='', max_length=254, null=True, verbose_name='Электронная почта')),
                ('phone', models.CharField(blank=True, max_length=250, null=True, verbose_name='Телефон')),
                ('web_site', models.CharField(blank=True, max_length=250, null=True, verbose_name='Веб-сайт')),
                ('bin', models.CharField(blank=True, default='000000000000', max_length=15, null=True, verbose_name='БИН')),
                ('chairman_upr', models.CharField(blank=True, max_length=250, null=True, verbose_name='Председатель правления')),
                ('heads', models.CharField(blank=True, max_length=250, null=True, verbose_name='Совет Директоров')),
                ('members', models.CharField(blank=True, max_length=250, null=True, verbose_name='Члены Правления')),
                ('accountant', models.CharField(blank=True, max_length=250, null=True, verbose_name='Главный бухгалтер3')),
                ('bank', models.CharField(blank=True, max_length=250, null=True, verbose_name='Банк Второго уровня')),
                ('custodian', models.CharField(blank=True, max_length=250, null=True, verbose_name='Кастодиан')),
                ('brokers', models.CharField(blank=True, max_length=250, null=True, verbose_name='Брокеры-дилеры')),
            ],
            options={
                'verbose_name': 'Финансовые организации',
                'verbose_name_plural': 'Финансовые организации',
            },
        ),
    ]
