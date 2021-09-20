from django.conf.urls import url
# from django.urls import path

from product.views import CategoryListAPIView, SubCategoryListAPIView,ProductListCreateAPIView
 
# from product import views


urlpatterns = [

    url(r'^category/', CategoryListAPIView.as_view(), name="category_list"),
    url(r'^sub-category/', SubCategoryListAPIView.as_view(), name="sub-category_list"),
    url(r'^product/', ProductListCreateAPIView.as_view(), name="sub-category_list"),
   
#    path(r'Productsave/', views.productsaveList.as_view(),name="product_list"),
]
