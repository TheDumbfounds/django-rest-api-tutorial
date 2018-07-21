
from django.contrib import admin
from django.urls import path, include
from .router import router
from rest_framework.authtoken import views
from django.contrib.auth.views import login

urlpatterns = [
    path('snippets/', include('snippets.urls', namespace='snippets')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('login/', login, name='login')
]
