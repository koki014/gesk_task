from django.urls import path
from .views import PayloadList, PayloadDetail

urlpatterns = [
    path('',PayloadList.as_view(),name='payload_list'),
    path('<int:pk>/',PayloadDetail.as_view(),name='payload_detail'),
]