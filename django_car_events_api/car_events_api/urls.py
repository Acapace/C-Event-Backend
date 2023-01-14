from django.urls import path
from . import views

urlpatterns = [
    # api/blog will be routed to the BlogList view for handling
    path('api/blog', views.BlogList.as_view(), name='blog_list'),
    # api/blog will be routed to the Blog   Detail view for handling
    path('api/blog/<int:pk>', views.BlogDetail.as_view(), name='blog_detail'),
]

urlpatterns += [
    path('api/inventory', views.InventoryList.as_view(), name='inventory_list'),
    path('api/inventory/<int:pk>',
         views.InventoryDetail.as_view(), name='inventory_detail'),
]

urlpatterns += [
    path('api/carplan', views.CarPlanList.as_view(), name='carplan_list'),
    path('api/carplan/<int:pk>',
         views.CarPlanDetail.as_view(), name='carplan_detail'),
]

urlpatterns += [
    path('api/carspecs', views.CarSpecsList.as_view(), name='carspecs_list'),
    path('api/carspecs/<int:pk>',
         views.CarSpecsDetail.as_view(), name='carspecs_detail'),
]
