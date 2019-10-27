from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('contacts.urls', namespace='contact')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
