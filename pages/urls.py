from django.urls import path, include
from rest_framework.routers import DefaultRouter

from pages.views import PageViewSet, PageComponentViewSet

router = DefaultRouter()
router.register(r'pages', PageViewSet, basename="page_viewset")
router.register(r'page/components', PageComponentViewSet, basename="page_components")

urlpatterns = [
    path('api/', include(router.urls)),
]
