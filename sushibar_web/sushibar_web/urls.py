from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('web/', include('web.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('main.urls')),
]
