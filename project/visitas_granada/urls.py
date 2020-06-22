from django.urls import path, include
from . import views
# Django rest api 
from django.conf.urls import url
from rest_framework import routers


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'visitas', views.VisitaViewSet)
router.register(r'comentarios', views.ComentarioViewSet)


urlpatterns = [
path('', views.index, name='index'),
path('detail/<int:pk>', views.detail_visita, name='detail'),
path('new/', views.add_visita, name='add_visita'),
path('post/<int:pk>', views.update_visita, name='update_visita'),
path('delete/<int:pk>', views.delete_visita, name='delete_visita'),
path('api/', include(router.urls)),
path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
path('api/likes/<int:pk>', views.likes_endpoint, name='likes'),
]