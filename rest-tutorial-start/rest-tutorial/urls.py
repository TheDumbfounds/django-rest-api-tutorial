
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('snippets/', include('snippets.urls', namespace='snippets')),
    path('admin/', admin.site.urls),
]
