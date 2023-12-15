from rest_framework import serializers
from .models import *


class FinancialOrganizationsSerializer(serializers.Serializer):
    class Meta:
        model = FinancialOrganization
        fields = ['full_name', 'chairman', 'email', 'phone', 'web_site', 'bin', 'chairman_upr', 'heads', 'members',
                  'accountant', 'bank', 'custodian',
                  'brokers', 'address']
