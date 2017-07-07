from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import ImageMetadata


@api_view(['GET', 'PATCH'])
@permission_classes((AllowAny, ))
def image_metadata(request):
    """
    Return image metadata.
    """
    if request.method == 'GET':
        try:
            image_metadata = ImageMetadata.objects.get(pk=1)
            return Response(image_metadata.content)
        except ImageMetadata.DoesNotExist:
            return Response({})

    elif request.method == 'PATCH':
        print(type(request.data['content']))
        try:
            image_metadata = ImageMetadata.objects.get(pk=1)
        except ImageMetadata.DoesNotExist:
            image_metadata = ImageMetadata()
        image_metadata.content = request.data['content']
        image_metadata.save()
        return Response(image_metadata.content, status=status.HTTP_201_CREATED)

def index(request):
    return render(request, 'index.html')