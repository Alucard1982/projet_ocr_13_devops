from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('sentry-debug/', views.trigger_error),
    path('', include('lettings.urls')),
    path('', include('profiles.urls')),
]
