
from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'blog'



# router = routers.DefaultRouter()
# router.register(r'blog', views.blog)


urlpatterns = [
    # url(r'', include(router.urls)),
    path('blog/', views.blog, name='index'),
    path('blog/<str:pk>', views.blog_detail, name='detail'),

    
]

