from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('DataFrame/', views.post_list, name='post_list'),
    path('', views.pricefilter, name='pricefilter'),
    path('contact/', views.contact, name='contact'),
    path('/<str:category>/', views.pricefilter, name='home_category'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('update/<int:pk>/', views.update, name='update'),
   
    #API endpoints
    path('price-category/', views.price_category, name='price_category'),
    path('api/my_context/', views.contact, name='api_my_context'),
    path('api/detail/', views.pricefilter, name='api_detail'),
    path('api/posts/', api_views.PostList.as_view(), name='api_post_list'),
    path('api/posts/<int:pk>/', api_views.PostDetail.as_view(), name='api_post_detail'),
    path('download-posts/', views.download_posts_excel, name='download_posts'),
    path('post_update/<int:pk>/', views.post_update, name='post_update')
]



# path('api/my_context/', views.contact, name='api_my_context'),


