from django.urls import path

from . import views

urlpatterns = [
    path('', views.notesPage, name='notesPage'),
    path('createNote', views.newNotePage, name='createNotePage'),
    path('viewNote/<id>', views.viewNote, name='viewNotePage')
]