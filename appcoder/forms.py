from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    comision = forms.IntegerField()
    email = forms.EmailField()

class BuscaCursoForm(forms.Form):
    curso = forms.CharField()