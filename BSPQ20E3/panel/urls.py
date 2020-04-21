from django.urls import path, include
from . import views

app_name = 'panel'

urlpatterns = [
    path('', views.index, name="index"),
    path('settings', views.settings),
    path('livelog', views.livelog, name="livelog"),
    path('accounts', views.accounts),
    
    #USER LOGIN TEST
    path('manage/', views.manage, name='manage'),
]