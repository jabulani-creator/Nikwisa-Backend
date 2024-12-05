from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Wedding
from .serializers import WeddingSerializer

class WeddingViewSet(ModelViewSet):
    queryset = Wedding.objects.all()
    serializer_class = WeddingSerializer

    def list(self, request):
        """Filter weddings by subcategory if provided."""
        subcategory_id = request.query_params.get("subcategory")
        if subcategory_id:
            self.queryset = self.queryset.filter(subcategory_id=subcategory_id)
        return super().list(request)

    def retrieve(self, request, pk=None):
        """Retrieve a specific wedding along with related weddings in the same subcategory."""
        try:
            wedding = Wedding.objects.get(pk=pk)
        except Wedding.DoesNotExist:
            return Response({"error": "Wedding not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(wedding)
        related_weddings = Wedding.objects.filter(subcategory=wedding.subcategory).exclude(id=wedding.id)
        related_serializer = self.get_serializer(related_weddings, many=True)

        return Response({
            "wedding": serializer.data,
            "related_weddings": related_serializer.data
        })



