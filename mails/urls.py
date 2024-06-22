from django.urls import path,include
from rest_framework.routers import DefaultRouter
from mails.views import MailViewSet, UserViewSet, RoleViewSet

app_name = 'mails'
router = DefaultRouter()
router.register(r'mails', MailViewSet)
router.register(r'users', UserViewSet)
router.register(r'roles', RoleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]