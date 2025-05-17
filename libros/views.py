from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, DetailView # importar las vistas de creación, lista y eliminación
from .models import Book # importar el modelo de libro
from django.urls import reverse_lazy # importar la función reverse_lazy para redirigir después de crear un libro

# Create your views here.

class BookCreateView(CreateView):
    template_name = 'post_create.html'  # plantilla para el formulario
    success_url=reverse_lazy("post_list")  # URL a la que redirigir después de crear el libro
    # modelo para la creación de libros
    model = Book
    fields = ['titulo', 'autor', 'fecha_publicacion', 'paginas', 'idioma', 'image']  # campos del formulario

class PostListView(ListView):
        template_name = 'post_list.html'
        model = Book  
        context_object_name = 'lista_de_objects' #cambia el nombre de la lista de objetos

class BookDeleteView(DeleteView): # vista para eliminar un libro
        template_name = "post_delete.html" # plantilla para la confirmación de eliminación
        model = Book # modelo para la eliminación
        success_url=reverse_lazy("post_list") # URL a la que redirigir después de eliminar el libro

class BookReadView(DetailView): # vista para leer un libro
        template_name = 'post_detail.html' # plantilla para la lectura del libro
        model = Book # modelo para la lectura
        context_object_name = 'post' #cambia el nombre de la lista de objetos
