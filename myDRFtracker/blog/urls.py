
from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'blog'



# router = routers.DefaultRouter()
# router.register(r'blog', views.BlogViewSets, basename = 'blog')
# blog_collection

urlpatterns = [
    # path(r'', include(router.urls)),
    path('post/', views.blog_collection, name='post'),

    path('report/', views.report, name='report'),

    
]

