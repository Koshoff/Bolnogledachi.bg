# core/urls.py
from django.urls import path
from bolnogledachi_bg.core.views import \
    home, contact_view, about_us, privacy_policy

urlpatterns = [
    path('', home, name='home'),
    path('contact_form/', contact_view, name='contact_form'),
    path('about_us/', about_us, name='about_us'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
]