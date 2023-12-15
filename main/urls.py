from django.contrib import admin
from django.urls import path, include
from FinNadzor.views import *
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
# router = routers.DefaultRouter()
# router.register(r'api/v1/finorg', FinancialOrganizationViewSet, basename='Финансовые организации')


urlpatterns = [
    path('api/financial-organizations/', csrf_exempt(FinancialOrganizationListView.as_view()), name='financial_organization_list'),
    # path('api/financial-organizations-post/', csrf_exempt(Postfin.as_view()), name='financial_orgaization_list'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
