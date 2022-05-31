from django import forms

class MeetingForm(forms.Form):
    titulo = forms.CharField(max_length=100, required=True)
    comienzo = forms.DateTimeField(required=True)
    cierre = forms.DateTimeField(required=True)
    direccion = forms.TextInput()
    


    class Meta:
        fields = [
            'titulo',
            'host',
            'comienzo',
            'cierre',
            'ciudad',
            'direccion',
            'categoria'
        ]


