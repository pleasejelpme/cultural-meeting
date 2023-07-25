from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView
from django.db.models import Q
from django.contrib import messages
import datetime

from .models import Categoria, Meeting, Comentario
from .forms import MeetingForm


now = datetime.date.today()

def meeting_detail_view(request, pk):
    meeting = Meeting.objects.get(id=pk)
    asistentes = meeting.asistentes.all
    comentarios = meeting.comentario_set.all()

    if request.user.is_authenticated and request.method == 'POST':
        if 'unirse' in request.POST:
            for asistente in meeting.asistentes.all():
                if request.user == asistente:
                    raise ValueError('Ya te has unido a este meeting')
            meeting.asistentes.add(request.user)
            return redirect('meeting-detail', pk)
        
        if 'comentar' in request.POST:
            Comentario.objects.create(
                usuario = request.user,
                meeting = meeting,
                comentario = request.POST.get('comentar')
            )
            messages.success(request, 'Comentario publicado!')
            return redirect('meeting-detail', pk)

    context = {
        'meeting':meeting,
        'asistentes':asistentes,
        'comentarios':comentarios
        }

    return render(request, 'detail.html', context)



class ComentarioDeleteView(DeleteView):
    model = Comentario
    template_name = "delete.html"
    context_object_name = 'comentario'
    success_url = reverse_lazy('home')
    
    def get(self, request, pk, *args, **kwargs):
        comentario = Comentario.objects.get(id=pk)
        if request.user != comentario.usuario:
            messages.error(request, 'No autorizado')
            return redirect('home')
        return super(ComentarioDeleteView, self).get(request, pk, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        messages.success(request, 'Comentario eliminado')
        return super().post(request, *args, **kwargs)


class MeetingCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Meeting
    form_class = MeetingForm
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.host = self.request.user
        self.object = form.save()
        self.object.asistentes.add(self.request.user)
        return redirect('home')
    
    def post(self, request, *args, **kwargs):
        messages.success(request, 'Meeting creado!')
        return super(MeetingCreateView, self).post(request, *args, **kwargs)


class MeetingsListView(ListView):
    model = Meeting
    template_name = 'list.html'
    context_object_name = 'meetings'


def home_view(request):    
    categorias = Categoria.objects.all()
    user = request.user
    meetings_personalizados = Meeting.objects.filter(
        Q(ciudad = user.ciudad_origen) &
        Q(categoria__in = user.intereses.all())
    ).order_by('-comienzo')

    q = request.GET.get('q') if request.GET.get('q') != None else ''
    meetings = Meeting.objects.filter(
        Q(cierre__gte = now) &
        Q(      
            Q(categoria__categoria__icontains = q) |
            Q(titulo__icontains = q)
        )
    )
    
    meeetings_count = meetings.count()

    context = {
        'categorias':categorias,
        'meetings':meetings,
        'meetings_count':meeetings_count,
        'meetings_personalizados':meetings_personalizados,
    }

    return render(request, 'home.html', context)


class PreferencesBasedListView(LoginRequiredMixin, ListView):
    model = Meeting
    template_name = 'home.html'
    context_object_name = 'meetings'
    login_url = 'login'

    def get_queryset(self):
        user = self.request.user
        queryset = Meeting.objects.all().filter(
            Q(categoria__in = user.intereses.all()) &
            Q(cierre__gte = now)
        )
        return queryset






