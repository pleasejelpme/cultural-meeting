from django.urls import path
from .views import PerfilCreateView, PerfilLoginView, PerfilDetailView

urlpatterns = [
    path('register/', PerfilCreateView.as_view(), name='register'),
    path('login/', PerfilLoginView.as_view(), name='login'),
    path('usuario/<int:pk>', PerfilDetailView.as_view(), name='perfil-detail'),
]