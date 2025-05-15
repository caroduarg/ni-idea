from django.urls import path, include
from .views import SignUpView, home

urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    # URL para la vista de inicio, aqui se llama la vista home que se hizo en auth/views.py
    path('', home, name='home'),
]