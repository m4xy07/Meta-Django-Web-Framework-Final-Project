from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"), 
    path('menu/', views.menu, name="menu"),
    path('menu/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('menu/items/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu/items/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    path('api-token-auth/', obtain_auth_token),
]
