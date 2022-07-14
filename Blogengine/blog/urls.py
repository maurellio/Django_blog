from django.urls import path
from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='current_post_url'),
    path('tags/', tag_list, name='tag_list_url'),
    path('tag/<str:slug>', TagDetail.as_view(), name='tag_detail_url')
]