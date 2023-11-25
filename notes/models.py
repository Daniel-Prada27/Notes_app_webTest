from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=30)
    note_body = models.CharField(max_length=200)
    creation_date = models.DateField()
    def __str__(self):
        return self.title

