from django.urls import path
from django.views.generic import RedirectView
from .views import lista_eventos, login_user, submit_login, logout_user, evento, submit_evento


urlpatterns = [
    path('agenda/', lista_eventos, name='agenda'),
    path('', RedirectView.as_view(url='agenda/')),
    path('agenda/evento/', evento, name='evento'),
    path('agenda/evento/submit', submit_evento, ),
    path('login/', login_user, name='login_user'),
    path('login/submit', submit_login),
    path('logout/', logout_user, name='logout_user'),
]

