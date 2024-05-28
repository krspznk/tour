from django.urls import path, include
from . import views
from .views import CityViewSet, TranspontViewSet, HotelViewSet, ExcursionViewSet, TourViewSet, TourOrderViewSet, OrderViewSet, QuestionViewSet
from rest_framework.routers import DefaultRouter
from .views import data_table



router = DefaultRouter()
router.register(r'cities', CityViewSet)
router.register(r'transponts', TranspontViewSet)
router.register(r'hotels', HotelViewSet)
router.register(r'excursions', ExcursionViewSet)
router.register(r'tours', TourViewSet)
router.register(r'tour-orders', TourOrderViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('tourpage/', views.tour_page, name='tourpage'),  
    path('hotelpage/', views.hotel_page, name='hotelpage'),  
    path('excursionpage/', views.excursion_page, name='excursionpage'),  
    path('transportpage/', views.transport_page, name='transportpage'),  
    path('login/', views.Login, name ='login'),
    path('user_profile/', views.user_profile, name='user_profile'), 
    path('register/', views.register, name ='register'),
    path("tourpage/<slug:slug>", views.tour_details, name = "tourdetail"),
    path("hotelpage/<slug:slug>", views.hotel_details, name = "hoteldetail"),
    path("excursionpage/<slug:slug>", views.excursion_details, name = "excursiondetail"),
    path('tourpage/<slug:slug>/order', views.tour_order, name='tourorder'), 
    path('order/', views.order, name='order'), 
    path("success/", views.success, name ='success'), 
    path('logout/', views.logout_user, name='logout'),
    path('orders/', views.orders_view, name='orders'),
    path('all_services/', views.all_services_view, name='all_services'),
    path('all_services/add_transport', views.add_transport, name='add_transport'),
    path('all_services/add_hotel', views.add_hotel, name='add_hotel'),
    path('all_services/add_excursion', views.add_excursion, name='add_excursion'),
    path('all_services/add_tour', views.add_tour, name='add_tour'),
    path('transport/<int:transport_id>/delete/', views.delete_transport_view, name='delete_transport'),
    path('hotel/<int:hotel_id>/delete/', views.delete_hotel_view, name='delete_hotel'),
    path('excursion/<int:excursion_id>/delete/', views.delete_excursion_view, name='delete_excursion'),
    path('tour/<int:tour_id>/delete/', views.delete_tour_view, name='delete_tour'),
    path('api/', include(router.urls)),
    path('data-table/', data_table, name='data_table'),



]
