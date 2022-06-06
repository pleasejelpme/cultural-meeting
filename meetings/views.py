from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView, ListView, View
from django.db.models import Q

from profiles.models import Perfil
from .models import Categoria, Meeting
from .forms import MeetingForm


def meeting_detail_view(request, pk):
    meeting = Meeting.objects.get(id=pk)
    asistentes = meeting.asistentes.all

    if request.method == 'POST':
        asistentes_list = meeting.asistentes.all()
        
        for asistente in asistentes_list:
            if request.user == asistente:
                raise ValueError('Ya te has unido a este meeting')

        meeting.asistentes.add(request.user)
        return redirect('meeting-detail', pk)

    context = {
        'meeting':meeting,
        'asistentes':asistentes
        }
    return render(request, 'meetings/detail.html', context)


class MeetingCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Meeting
    form_class = MeetingForm
    template_name = 'meetings/create.html'

    def form_valid(self, form):
        form.instance.host = self.request.user
        self.object = form.save()
        self.object.asistentes.add(self.request.user)
        return redirect('home')


class MeetingsListView(ListView):
    model = Meeting
    template_name = 'meetings/list.html'
    context_object_name = 'meetings'


def home_view(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    categorias = Categoria.objects.all()
    meetings = Meeting.objects.filter(
        Q(categoria__categoria__icontains = q) |
        Q(titulo__icontains = q)
    )
    
    meeetings_count = meetings.count()

    context = {
        'categorias':categorias,
        'meetings':meetings,
        'meetings_count':meeetings_count
    }

    return render(request, 'meetings/home.html', context)



class PreferencesBasedListView(LoginRequiredMixin, ListView):
    model = Meeting
    template_name = 'meetings/home.html'
    context_object_name = 'meetings'
    login_url = 'login'

    def get_queryset(self):
        user = self.request.user
        queryset = Meeting.objects.all().filter(
            categoria__in = user.intereses.all()
        )
        return queryset





