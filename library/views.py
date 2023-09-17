from django.shortcuts import render
from . import models

def program_book_view(request):
    book = models.ProgramBook.objects.all()
    return render(request, 'library.html', {'book_key': book})
