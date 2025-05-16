from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.

class SignUpView (CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('post_list') # URL a la que se redirige después de un registro exitoso

#mostrar la pagina de inicio
def home(request):
    return render(request, 'registration/home.html')