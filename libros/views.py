from django.shortcuts import render
from django.views.generic import CreateView # impartar la vista de creación
from .models import Book # importar el modelo de libro

# Create your views here.

class BookCreateView(CreateView):
    template_name = 'post_create.html'  # plantilla para el formulario
    success_url = '/libros/'  # URL a la que redirigir después de crear el libro
    # modelo para la creación de libros
    model = Book
    fields = ['titulo', 'autor', 'fecha_publicacion', 'paginas', 'idioma', 'image']  # campos del formulario
