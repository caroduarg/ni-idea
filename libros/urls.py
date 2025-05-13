from django.urls import path # importar la funcion path para crear la URL
from libros.views import BookCreateView, PostListView # importar las vistas necesarias

urlpatterns = [
    path('post', PostListView.as_view(), name='post_list'), # URL para la lista de libros
    path('create/', BookCreateView.as_view(), name='post_create'), # URL para crear un nuevo libro

]