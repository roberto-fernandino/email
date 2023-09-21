# urls.py
from django.urls import path
from .views import relatorio


app_name = "home"

# urls donw here
urlpatterns = [
    path('', relatorio, name='home-relatorio')
]

