from django.contrib import admin
from .models import Executive, FinancialOrganization, Employment

admin.site.site_header = 'Панель администратора'

admin.site.register(Executive)
admin.site.register(FinancialOrganization)
admin.site.register(Employment)

