from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from libros.views import lista_libros, detalle_libros, home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home, name='home'),
    url(r'^home/',home, name='home'),
    url(r'^lista/',lista_libros, name='Vista'),
    url(r'^detalles/(?P<id>\d)/$', detalle_libros, name='Detalles'),
]
