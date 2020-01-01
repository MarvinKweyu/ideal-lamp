from django.urls import path
from . import views


app_name = 'solos'

urlpatterns = [
    path('', views.index, name='home'),
    # path('', views.ListSearchResult.as_view(), name='home'),
]