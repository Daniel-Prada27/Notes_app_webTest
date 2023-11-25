from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from .models import Note


# Create your views here.

def notesPage(request):

    notes_list = Note.objects.all()
    
    paginator = Paginator(notes_list, 5)

    page_number = request.GET.get('page', 0)
    page_obj = paginator.get_page(page_number)

    template = loader.get_template("mostrarNotas.html")
    context = {"page_obj": page_obj}
    return HttpResponse(template.render(context, request))