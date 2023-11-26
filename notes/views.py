from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from .models import Note
from .forms import NoteForm
from datetime import datetime
from django.shortcuts import redirect,get_object_or_404

# Create your views here.

def notesPage(request):

    notes_list = Note.objects.all()
    # notes_list = notes_list.reverse()
    paginator = Paginator(notes_list, 5)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    template = loader.get_template("mostrarNotas.html")
    context = {"page_obj": page_obj}
    return HttpResponse(template.render(context, request))

def newNotePage(request):

    template = loader.get_template("crearNota.html")
    #Generar Formulario
    if request.method == "POST":
        form = NoteForm(request.POST or None, request.FILES)
        if form.is_valid():
            #obtener datos del formulario
            new_note = form.save(commit=False)
            #Asignar fecha de creación
            new_note.creation_date = datetime.now()
            #Guardar Producto
            new_note.save()
            return redirect('notesPage')
    else:
        form = NoteForm()
    #Crear contexto
    context = {}
    context['form'] = form
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

def editNotePage(request,id):
    #Obtener el template
    template = loader.get_template("editarNota.html")
    #Buscar Producto
    obj = get_object_or_404(Note, id = id)
    #formulario que contiene la instancia
    form = NoteForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('notesPage')   
    #Agregar el contexto
    context = {}
    context['form'] = form
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

def deleteNotePage(request, id):
    template = loader.get_template("eliminarNota.html")
    #Buscar el producto
    obj = get_object_or_404(Note, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect('notesPage')
    #Agregar el contexto
    context = {"note": obj}
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

def viewNotePage(request, id, page):
    note = Note.objects.get(id=id)
    page_number = page
    template = loader.get_template("verNota.html")
    context = {'note': note, "page": page_number}
    return HttpResponse(template.render(context,request))