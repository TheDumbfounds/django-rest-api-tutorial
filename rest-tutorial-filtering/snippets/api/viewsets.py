from snippets.models import Snippet
from .serializers import SnippetSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters  import rest_framework as filters


class SnippetFilter(filters.FilterSet):

    class Meta:
        model = Snippet
        fields = {
            'title': ['icontains'],
            'created': ['iexact', 'lte', 'gte'],
        }


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    filterset_class = SnippetFilter

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)
