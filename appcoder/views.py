from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def inicio(request):
    return render(request,"appcoder/inicio.html")

def cursos(request):
    
    cursos = Curso.objects.all()
    
    return render(request,"appcoder/cursos.html", {"cursos":cursos})

def estudiantes(request):
    return render(request,"appcoder/estudiantes.html")

def profesores(request):
    return render(request,"appcoder/profesores.html")

def entregables(request):
    return render(request,"appcoder/entregables.html")

def cursoFormulario(request):
    
    if request.method == 'POST':
    
        curso =  Curso(nombre = request.POST['curso'], comision = request.POST['comision'])
        curso.save()
        
        return render(request, "appcoder/inicio.html")
    
    return render(request,"appcoder/cursoFormulario.html")

def estudianteFormulario(request):
    
    if request.method == 'POST':
    
        estudiante =  Estudiante(nombre = request.POST['nombre'],apellido = request.POST['apellido'], mail = request.POST['mail'])
        estudiante.save()
        
        return render(request, "appcoder/inicio.html")
    
    return render(request,"appcoder/estudianteFormulario.html")

def profesorFormulario(request):
    
    if request.method == 'POST':
    
        profesor =  Profesor(nombre = request.POST['nombre'],apellido = request.POST['apellido'], mail = request.POST['mail'], profesion = request.POST['profesion'])
        profesor.save()
        
        return render(request, "appcoder/inicio.html")
    
    return render(request,"appcoder/profesorFormulario.html")

def entregableFormulario(request):
    
    if request.method == 'POST':
    
        entregable =  Entregable(nombre = request.POST['nombre'], fecha = request.POST['fecha'], entrega = request.POST['entrega']=='on')
        entregable.save()
        
        return render(request, "appcoder/inicio.html")
    
    return render(request,"appcoder/entregableFormulario.html")


def formApi(request):

    if request.method == "POST":
            miFormulario = CursoFormulario(request.POST) 
            
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                
                curso = Curso(nombre=informacion["curso"], comision=informacion["comision"])
                curso.save()
                return render(request, "appcoder/inicio.html")
    else:
            miFormulario = CursoFormulario()

    return render(request, "appcoder/form-api.html", {"miFormulario": miFormulario})

def buscar_form_con_api(request):
    if request.method == "POST":
        miformulario = BuscaCursoForm(request.POST) # Aqui me llega la informacion del html

        if miformulario.is_valid():
            informacion = miformulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "appcoder/mostrar_cursos.html", {"cursos": cursos})
    else:
        miformulario = BuscaCursoForm()

    return render(request, "appcoder/buscar_form_con_api.html", {"miformulario": miformulario})