from django.urls import path
from .views import vista_1, vista_2

urlpatterns = [
    path('', vista_1),
    path('template-1/', vista_2),
]