# seat/ urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SeatViewSet, SeatListCreateView, get_seat_data_by_bus, update_seat_status

router = DefaultRouter()
router.register(r'seats', SeatViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
    path('api/seat/by-bus/<int:bus_id>/', get_seat_data_by_bus),
    path('api/seats/<int:seat_id>/status/', update_seat_status),  # 좌석 상태 업데이트 API
]