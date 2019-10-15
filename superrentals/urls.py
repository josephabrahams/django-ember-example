"""
URL Configuration
"""

from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'rentals', views.RentalViewSet)

urlpatterns = [
    # if ember is mounted at the root you need to define each route
    # instead of using a catch all, otherwise django will serve
    # the ember application insteda of the 404 page
    path('', views.ember),
    re_path(r'^about/?$', views.ember),
    re_path(r'^contact/?$', views.ember),
    re_path(r'^rentals/?$', views.ember),
    re_path(r'^rentals/.*/?$', views.ember),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework'))
]
