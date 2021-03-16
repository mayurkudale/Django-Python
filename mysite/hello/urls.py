from django.urls import path
from . import views
#from django.views.generic import TemplateView

app_name='hello'
urlpatterns = [
    path('', views.cookie),
    path('cookie', views.cookie),
    path('sessfun', views.sessfun),
]

