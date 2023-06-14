from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('restaurants/', views.restaurants_index, name='index'),
	path('restaurants/<int:restaurant_id>', views.restaurants_detail, name='detail'),
    path('restaurants/<int:restaurant_id>/add_menu_item/', views.add_menu_item, name='add_menu_item'),
	path('restaurants/create/', views.RestaurantCreate.as_view(), name='restaurants_create'),
    path('restaurants/<int:pk>/update/', views.RestaurantUpdate.as_view(), name='restaurants_update'),
    path('restaurants/<int:pk>/delete', views.RestaurantDelete.as_view(), name='restaurants_delete'),
    path('menu_items/<int:pk>/update', views.Menu_itemUpdate.as_view(), name='menu_items_update'),
    path('menu_items/<int:pk>/delete', views.Menu_itemDelete.as_view(), name='menu_items_delete'),
    path('orders/<int:pk>/update', views.OrderUpdate.as_view(), name='orders_update'),
    path('orders/<int:pk>/delete', views.OrderDelete.as_view(), name='orders_delete'),
	path('accounts/signup/', views.signup, name='signup'),
    path('restaurants/<int:restaurant_id>/add_order/', views.add_order, name='add_order'),
	path('orders/<int:order_id>', views.orders_detail, name='order_detail'),

]