from django.db import models
import uuid


class FinancialOrganization(models.Model):
    full_name = models.CharField(verbose_name='Полное наименование', max_length=250, null=True, blank=True)
    chairman = models.CharField(verbose_name='Председатель', max_length=250, null=True, blank=True)
    email = models.EmailField(verbose_name='Электронная почта', default='', null=True, blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=250, null=True, blank=True)
    web_site = models.CharField(verbose_name='Веб-сайт', max_length=250, null=True, blank=True)
    bin = models.CharField(verbose_name='БИН', max_length=15, default='000000000000', null=True, blank=True)
    chairman_upr = models.CharField(verbose_name='Председатель правления', max_length=250, null=True, blank=True)
    heads = models.CharField(verbose_name='Совет Директоров', max_length=250, null=True, blank=True)
    members = models.CharField(verbose_name='Члены Правления', max_length=250, null=True, blank=True)
    accountant = models.CharField(verbose_name='Главный бухгалтер', max_length=250, null=True, blank=True)
    bank = models.CharField(verbose_name='Банк Второго уровня', max_length=250, null=True, blank=True)
    custodian = models.CharField(verbose_name='Кастодиан', max_length=250, null=True, blank=True)
    brokers = models.CharField(verbose_name='Брокеры-дилеры', max_length=250, null=True, blank=True)
    address = models.CharField(verbose_name='Адрес', max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to='financial_organization_images/', null=True, blank=True)

    class Meta:
        verbose_name = 'Финансовые организации'
        verbose_name_plural = 'Финансовые организации'

    def __str__(self):
        return str(self.full_name)


class Executive(models.Model):
    full_name = models.CharField(verbose_name='ФИО', max_length=250, null=True, blank=True)
    iin = models.CharField(verbose_name='ИИН', max_length=15, default='000000000000', null=True, blank=True)
    position = models.CharField(verbose_name='Должность', max_length=250, null=True, blank=True)
    contacts = models.CharField(verbose_name='Контактная информация', max_length=250, null=True, blank=True)
    employments = models.ManyToManyField(FinancialOrganization, through='Employment')

    class Meta:
        verbose_name = 'Руководители'
        verbose_name_plural = 'Руководители'

    def __str__(self):
        return str(self.full_name)


class Employment(models.Model):
    executive = models.ForeignKey(Executive, on_delete=models.CASCADE)
    organization = models.ForeignKey(FinancialOrganization, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ('executive', 'organization', 'start_date', 'end_date')

    def __str__(self):
        return str(self.executive)

