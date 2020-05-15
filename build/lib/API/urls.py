from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers

app_name = 'API'

router = routers.DefaultRouter()
router.register(r'API/users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]