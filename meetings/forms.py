from django import forms
from .models import Meeting
import datetime
import pytz

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = [
            'titulo',
            'descripcion',
            'comienzo',
            'cierre',
            'ciudad',
            'direccion',
            'categoria'
        ]
    
        widgets = {
            'comienzo' : forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'cierre' : forms.DateTimeInput(attrs={'type':'datetime-local'})
        }

    def clean(self):
        now = datetime.datetime.now()
        now = pytz.utc.localize(now)

        comienzo = self.cleaned_data['comienzo']
        cierre = self.cleaned_data['cierre']

        if comienzo < now or cierre <= comienzo:
            raise forms.ValidationError('Fechas invalidas!')
            
        return super(MeetingForm, self).clean()
    
    
    


