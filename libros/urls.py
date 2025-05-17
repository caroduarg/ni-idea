from django.urls import path # importar la funcion path para crear la URL
from libros.views import BookCreateView, PostListView, BookDeleteView, BookReadView, PostUpdate # importar las vistas necesarias

urlpatterns = [
    path('post', PostListView.as_view(), name='post_list'), # URL para la lista de libros
    path('create/', BookCreateView.as_view(), name='post_create'), # URL para crear un nuevo libro
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='post_delete'), # URL para eliminar un libro
    path('post/<int:pk>/', BookReadView.as_view(), name='post_read'), # URL para leer un libro
    path('update/<int:pk>/', PostUpdate.as_view(), name='post_update'),
]