from django.contrib import admin
from django.urls import path
from portfolio.views import portfolio_home, contact_email, codewill_coming_soon, fake_admin
from django.conf import settings
from django.conf.urls.static import static
handler404 = 'portfolio.views.custom_404'

urlpatterns = [
    path('admin/', fake_admin, name='admin'),
    path('sujkusu2812/', admin.site.urls),
    path('', portfolio_home, name='home'),
    path('contact/', contact_email, name='contact_email'),
    path('codewill/', codewill_coming_soon, name='codewill_coming_soon'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
