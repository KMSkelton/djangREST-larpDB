from attributes.models import Attribute
from attributes.serializers import AttributeSerializer
from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# create generic view for handling GET and POST requests
class AttributeListCreate(generics.ListCreateAPIView):
  queryset = Attribute.objects.all()
  serializer_class = AttributeSerializer

class AttributeDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    """
    Retrieve, update or delete a Attribute instance.
    """
    def get_object(self, pk):
        try:
            return Attribute.objects.get(pk=pk)
        except Attribute.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        content = {
            'user': unicode(request.user),
            'auth': unicode(request.auth)            
        }
        snippet = self.get_object(pk)
        serializer = AttributeSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = AttributeSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)