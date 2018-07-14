
from django.contrib import admin
from django.urls import path, include
from .router import router

urlpatterns = [
    path('snippets/', include('snippets.urls', namespace='snippets')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls), name='api')
]
