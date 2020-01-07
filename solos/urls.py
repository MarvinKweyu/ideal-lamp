from django.urls import path
from . import views


app_name = 'solos'

urlpatterns = [
    path('', views.index, name='home'),
    # path('', views.ListSearchResult.as_view(), name='home'),
    # path('solos/<int:pk>/', views.SoloDetailView.as_view()),
    path('recordings/<slug:album>/<slug:track>/<slug:artist>/', views.SoloDetailView.as_view(), name='solo_detail_view'),
]
