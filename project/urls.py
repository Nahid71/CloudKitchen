from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('', include('contacts.urls', namespace='contact')),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),

]
