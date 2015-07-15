from rest_framework import routers
from api import views
from django.conf.urls import include, url
from django.contrib import admin
from api.views import parser

router = routers.DefaultRouter()
router.register(r'games', views.GameViewSet)
router.register(r'news', views.NewsViewSet)
router.register(r'streams', views.StreamViewSet)
router.register(r'matches', views.MatchViewSet)
router.register(r'videos', views.VideoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^get', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^parser', parser)
]
