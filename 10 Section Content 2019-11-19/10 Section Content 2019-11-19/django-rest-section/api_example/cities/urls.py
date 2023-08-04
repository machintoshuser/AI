from django.contrib import admin
from django.urls import path, include

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cities', views.CityView, base_name='cities')

from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title="Cities API", renderer_classes=[SwaggerUIRenderer, OpenAPIRenderer])

urlpatterns = [
    path('cities/',include(router.urls)),
    path('', schema_view, name='docs')
]
