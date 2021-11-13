from django.urls import path
from django.views.generic import RedirectView
from .views import lista_eventos, login_user, submit_login, logout_user


urlpatterns = [
    path('agenda/', lista_eventos, name='agenda'),
    path('', RedirectView.as_view(url='agenda/')),
    path('login/', login_user),
    path('login/submit', submit_login),
    path('logout/', logout_user),

]
