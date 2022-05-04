from django.urls import URLPattern, path
from .views import index
from .views import agenda
urlpatterns = [
    path('', index, name="index"),
    path('', agenda, name="agenda"),
]


