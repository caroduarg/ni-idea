from django.shortcuts import render
from django.views.generic import CreateView, ListView# importar las vistas de creación y lista
from .models import Book # importar el modelo de libro

# Create your views here.

class BookCreateView(CreateView):
    template_name = 'post_create.html'  # plantilla para el formulario
    success_url = '/libros/'  # URL a la que redirigir después de crear el libro
    # modelo para la creación de libros
    model = Book
    fields = ['titulo', 'autor', 'fecha_publicacion', 'paginas', 'idioma', 'image']  # campos del formulario

class PostListView(ListView):
        template_name = 'post_list.html'
        model = Book  
        context_object_name = 'lista_de_objects' #cambia el nombre de la lista de objetos
