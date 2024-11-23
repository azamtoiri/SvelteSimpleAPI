from PIL import Image, ImageDraw, ImageFont
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from pages.models import Page, Component, PageComponent
from pages.serializers import PageSerializer, PageComponentSerializer
from pages.validators import ComponentValidator


class PageViewSet(viewsets.ModelViewSet):
    """ViewSet for Page model. This viewset is used to create, update, delete and list pages."""
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    lookup_field = 'slug'

    @action(detail=True, methods=['post'])
    def update_layout(self, request, pk=None):
        page = self.get_object()
        page.layout = request.data['layout']
        page.save()
        return Response({'status': 'layout updated'})

    def create(self, request, *args, **kwargs):
        try:
            # logic to create a new page
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], url_path=r'placeholder/(?P<width>\d+)/(?P<height>\d+)')
    def get_placeholder_image(self, request, width, height):
        """ TEST Generate gradient image with given width and height"""
        width, height = int(width), int(height)
        image = Image.new('RGB', (width, height), color=(200, 200, 200))
        draw = ImageDraw.Draw(image)

        # create gradient
        for y in range(height):
            r = int(255 * (y / height))
            g = int(255 * (1 - y / height))
            b = 150
            draw.line([(0, y), (width, y)], fill=(r, g, b))
        font = ImageFont.load_default()
        response = HttpResponse(content_type="image/png")
        image.save(response, "PNG")
        return response


class PageComponentViewSet(viewsets.ModelViewSet):
    """ ViewSet for PageComponent model
        This viewset is used to create, update, delete and list page components.
        """
    queryset = PageComponent.objects.all()
    serializer_class = PageComponentSerializer

    def create(self, request, *args, **kwargs):
        component = Component.objects.get(id=request.data['component'])
        if 'content' not in request.data:
            request.data['content'] = ComponentValidator.get_default_content(component)

        ComponentValidator.validate_component(component, request.data['content'])
        return super().create(request)
