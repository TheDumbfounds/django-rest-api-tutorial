
from django.urls import path, include
from . import views

app_name = 'snippets'
urlpatterns = [
    path('', views.SnippetListView.as_view(), name='list'),
    path('<int:pk>/', views.SnippetDetailView.as_view(), name='detail')
]
