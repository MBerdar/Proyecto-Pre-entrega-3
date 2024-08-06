from django.urls import path
from appcoder.views import  *
from appcoder import views

urlpatterns = [
    path('', inicio, name="inicio"),
    path('cursos/', cursos, name="cursos"),
    path('estudiantes/', estudiantes, name="alumnos"),
    path('profesores/', profesores, name="profesores"),
    path('entregables/', entregables, name="entregas"),
    path('cursoFormulario/', views.cursoFormulario, name="CursoFormulario"),
    path('estudianteFormulario/', views.estudianteFormulario, name="estudianteFormulario"),
    path('profesorFormulario/', views.profesorFormulario, name="profesorFormulario"),
    path('entregableFormulario/', views.entregableFormulario, name="entregableFormulario"),
    path('form-api/', views.formApi, name="FormApi"),
    path('buscar-form-con-api/', views.buscar_form_con_api, name="Buscar_Form_Con_Api"),
]