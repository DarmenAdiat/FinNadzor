from django.shortcuts import render
from django.templatetags.static import static
import base64
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from rest_framework import viewsets, permissions, generics, status
from FinNadzor.serializers import *
from django.http import JsonResponse, HttpResponse
from django.views import View


class FinancialOrganizationListView(View):

    def get(self, request):
        organizations = FinancialOrganization.objects.all()
        data = [{'full_name': org.full_name, 'chairman': org.chairman, 'email': org.email, 'phone': org.phone,
                 'web_site': org.web_site, 'bin': org.bin, 'chairman_upr': org.chairman_upr, 'heads': org.heads,
                 'address': org.address, 'accountant': org.accountant, 'members': org.members, 'image_url': self.get_image_url(org)} for org in organizations]
        return JsonResponse(data, safe=False)

    def get_image_url(self, organization):
        if organization.image:
            with open(organization.image.path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
                return f"data:image/{organization.image.name.split('.')[-1]};base64,{encoded_string}"
        else:
            return static('path/to/default/image.jpg')
# Create your views here.
