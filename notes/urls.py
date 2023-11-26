from django.urls import path

from . import views

urlpatterns = [
    path('', views.notesPage, name='notesPage'),
    path('createNote', views.newNotePage, name='createNotePage'),
    path('editNote/<id>', views.editNotePage, name='editNotePage'),
    path('deleteNote/<id>', views.deleteNotePage, name='deleteNotePage'),
    path('viewNote/<id>', views.viewNotePage, name='viewNotePage')
]