from django import forms

class FormularioEmpleados(forms.Form):

    Empleados=(
        (1,'Nombre'),
        (2,'Descripcion'),
        (3,'fotografia'),
        
    )

    nombre=forms.CharField(
        required=True,
        max_length=5,
        label='Nombre Empleado: ',
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    descripcion=forms.CharField(
        required=False,
        max_length=20,
        widget=forms.Textarea(attrs={'class':'form-control mb-3'})
    )
    fotografia=forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    precio=forms.CharField(
        required=True,
        max_length=20,
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'})
    )
    tipo=forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class':'form-select mb-3'}),
        choices=Empleados
    )