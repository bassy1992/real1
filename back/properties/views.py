from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .models import Property, PropertyImage
from .serializers import PropertySerializer, PropertyImageSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
    @action(detail=False, methods=['get'])
    def by_status(self, request):
        status_param = request.query_params.get('status', None)
        if status_param and status_param != 'All':
            properties = Property.objects.filter(status=status_param)
        else:
            properties = Property.objects.all()
        serializer = self.get_serializer(properties, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def upload_image(self, request, pk=None):
        """Upload an image file for a property"""
        property_obj = self.get_object()
        
        image_file = request.FILES.get('image')
        url = request.data.get('url')
        caption = request.data.get('caption', '')
        order = request.data.get('order', 0)
        
        if not image_file and not url:
            return Response(
                {'error': 'Either image file or URL must be provided'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        property_image = PropertyImage.objects.create(
            property=property_obj,
            image=image_file if image_file else None,
            url=url if url else None,
            caption=caption,
            order=order
        )
        
        serializer = PropertyImageSerializer(property_image, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['post'])
    def add_image_url(self, request, pk=None):
        """Add an image URL to a property"""
        property_obj = self.get_object()
        url = request.data.get('url')
        
        if not url:
            return Response(
                {'error': 'URL is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        caption = request.data.get('caption', '')
        order = request.data.get('order', 0)
        
        property_image = PropertyImage.objects.create(
            property=property_obj,
            url=url,
            caption=caption,
            order=order
        )
        
        serializer = PropertyImageSerializer(property_image, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
