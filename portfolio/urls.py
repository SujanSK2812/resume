from django.urls import path
from .views import portfolio_home, contact_email, codewill_coming_soon

urlpatterns = [
    path("", portfolio_home, name="home"),
    path("contact/", contact_email, name="contact_email"),
    path("codewill/", codewill_coming_soon, name="codewill_coming_soon"),
]
