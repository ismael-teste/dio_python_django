from django.urls import path
from .views import lista_eventos
from django.views.generic import RedirectView

urlpatterns = [
    path('agenda/', lista_eventos, name='agenda'),
    path('', RedirectView.as_view(url='agenda/')),

]
