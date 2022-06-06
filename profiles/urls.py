from django.urls import path
from .views import PerfilCreateView, PerfilLoginView, PerfilDetailView, logout_user

urlpatterns = [
    path('register/', PerfilCreateView.as_view(), name='register'),
    path('login/', PerfilLoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('usuario/<int:pk>', PerfilDetailView.as_view(), name='perfil-detail'),
]