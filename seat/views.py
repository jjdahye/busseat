# seat/views.py
from rest_framework import viewsets, generics
from .models import Seat, Bus, Stop
from .serializers import SeatSerializer
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status

# 좌석 상태 업데이트 API
@api_view(['PATCH'])
def update_seat_status(request, seat_id):
    try:
        seat = Seat.objects.get(id=seat_id)
        status = request.data.get('status')

        if status not in [Seat.OCCUPIED, Seat.AVAILABLE]:
            return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)

        seat.status = status
        seat.save()
        return Response({'message': 'Seat status updated successfully'}, status=status.HTTP_200_OK)
    except Seat.DoesNotExist:
        return Response({'error': 'Seat not found'}, status=status.HTTP_404_NOT_FOUND)

# 기존 코드 유지
class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

@api_view(['GET'])
def get_seat_data_by_bus(request, bus_id):
    try:
        bus = Bus.objects.get(id=bus_id)
        seats = Seat.objects.filter(bus=bus)
        seat_data = {seat.seat_number: seat.status for seat in seats}
        return Response(seat_data)
    except Bus.DoesNotExist:
        return Response({'error': 'Bus not found'}, status=status.HTTP_404_NOT_FOUND)

class SeatListCreateView(generics.ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer