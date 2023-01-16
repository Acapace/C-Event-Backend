from django.urls import path
from . import views

urlpatterns = [
    # api/blog will be routed to the BlogList view for handling
    path('api/blog', views.BlogList.as_view(), name='blog_list'),
    # api/blog will be routed to the Blog   Detail view for handling
    path('api/blog/<int:pk>', views.BlogDetail.as_view(), name='blog_detail'),
]

urlpatterns += [
    path('api/vendors', views.VendorList.as_view(), name='vendor_list'),
    path('api/vendors/<int:pk>',
         views.VendorDetail.as_view(), name='vendor_detail'),
]

urlpatterns += [
    path('api/categories', views.CategoryList.as_view(), name='category_list'),
    path('api/categories/<int:pk>',
         views.CategoryDetail.as_view(), name='category_detail'),
]

urlpatterns += [
    path('api/products', views.ProductList.as_view(), name='product_list'),
    path('api/poducts/<int:pk>',
         views.ProductDetail.as_view(), name='product_detail'),
]

urlpatterns += [
    path('api/options', views.OptionList.as_view(), name='option_list'),
    path('api/options/<int:pk>',
         views.OptionDetail.as_view(), name='option_detail'),
]

urlpatterns += [
    path('api/cars', views.CarList.as_view(), name='car_list'),
    path('api/cars/<int:pk>',
         views.CarDetail.as_view(), name='car_detail'),
]
