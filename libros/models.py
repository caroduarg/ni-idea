from django.db import models

# Create your models here.
# models para la creación de libros
class Book(models.Model):
    titulo = models.CharField(max_length=200) # título del libro
    autor = models.CharField(max_length=100, blank=True, null=True)  # Ejemplo para 'autor'  # autor del libro
    fecha_publicacion = models.DateField() # fecha de publicación
    paginas = models.IntegerField() # número de páginas
    idioma = models.CharField(max_length=30) # idioma del libro
    image = models.ImageField(upload_to='static/upload_images', verbose_name='Image', blank=True, null=True)
    # imagen del libro
    
    def __str__(self):
        return self.title
