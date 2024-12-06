from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import DeliveryOrder, DeliveryStatus
from .serializers import DeliveryOrderSerializer, DeliveryOrderUpdateSerializer

class DeliveryOrderViewSet(viewsets.ModelViewSet):
    queryset = DeliveryOrder.objects.all()
    serializer_class = DeliveryOrderSerializer

    @action(detail=True, methods=['put'])
    def update_status(self, request, pk=None):
        """Обновление статуса заявки."""
        order = self.get_object()
        serializer = DeliveryOrderUpdateSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """Удаление заявки, только если статус - CREATED."""
        order = self.get_object()
        if order.status != DeliveryStatus.CREATED:
            return Response(
                {"error": "Cannot delete order with status other than 'CREATED'"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().destroy(request, *args, **kwargs)