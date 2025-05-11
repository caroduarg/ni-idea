from django.urls import path # importar la funcion path para crear la URL
from libros.views import BookCreateView # importar la vista de creación de libros

urlpatterns = [
    path('create/', BookCreateView.as_view(), name='post_create'), # URL para crear un nuevo libro
]