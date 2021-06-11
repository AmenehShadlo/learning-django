from django.urls import path
from ticketSales import views


urlpatterns = [
    path('concert/list', views.concertListView),
    path('location/list', views.locationListView),
    path('concert/<int:concert_id>', views.concertDetailsView),
    path('time/list', views.timeView),
    path('concertEdit/<int:concert_id>', views.consertEditView),
]