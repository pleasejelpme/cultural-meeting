from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView, ListView, View

from profiles.models import Perfil
from .models import Categoria, Meeting
from .forms import MeetingForm


class MeetingDetailView(DetailView):
    model = Meeting
    context_object_name = 'meeting'
    template_name = "meetings/detail.html"


class MeetingCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Meeting
    form_class = MeetingForm
    template_name = 'meetings/create.html'

    def form_valid(self, form):
        form.instance.host = self.request.user
        self.object = form.save()
        Meeting.asistentes.add(self.request.user)
        return redirect('home')


# class JoinMeetingView(LoginRequiredMixin, UpdateView):
#     model = Meeting
#     template_name = 'meetings/join.html'
#     login_url = 'login'

#     def post(self, *args, **kwargs):
#         user = self.request.user
#         Meeting.asistentes.add(user)
#         return redirect('home')    




class MeetingsListView(ListView):
    model = Meeting
    template_name = 'meetings/list.html'
    context_object_name = 'meetings'




class PreferencesBasedListView(ListView):
    model = Meeting
    template_name = 'meetings/home.html'
    context_object_name = 'meetings'

    def get_queryset(self):
        user = self.request.user
        queryset = Meeting.objects.all().filter(
            categoria__in = user.intereses.all()
        )
        return queryset





