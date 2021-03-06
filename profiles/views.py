from django.shortcuts import redirect
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView

from .models import Perfil
from .forms import RegisterForm


class PerfilCreateView(CreateView):
    model = Perfil
    form_class = RegisterForm
    template_name = "register.html"
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(PerfilCreateView, self).form_valid(form)
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super(PerfilCreateView, self).get(request, *args, **kwargs)

class PerfilLoginView(LoginView):
    template_name= 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super(PerfilLoginView, self).get(request, *args, **kwargs)


def logout_user(request):
    logout(request)
    return redirect('login')


class PerfilDetailView(DetailView):
    model = Perfil
    context_object_name = 'user'
    template_name = 'perfil_detail.html'
