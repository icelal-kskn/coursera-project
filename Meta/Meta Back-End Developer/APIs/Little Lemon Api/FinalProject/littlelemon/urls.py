from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from littlelemon.views import *

urlpatterns = [
    path("menu-items", MenuItemsView.as_view()),
    path('menu-items/<int:pk>', MenuItemView.as_view()),
    path('groups/manager/users', ManagersGroup.as_view(group_name="manager")),
    path('groups/delivery-crew/users', ManagersGroup.as_view(group_name="delivery_crew")),
    path('groups/manager/users/<int:pk>', ManagerSingle.as_view(group_name="manager")),
    path('groups/delivery-crew/users<int:pk>', ManagerSingle.as_view(group_name="delivery_crew")),
    path('cart/menu/items', CartView.as_view()),
    path('orders/', OrdersView.as_view()),
    path('orders/<int:pk>', OrderSingleView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
