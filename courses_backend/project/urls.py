from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"view", views.ProjectAPI)

urlpatterns = [
    path('', include(router.urls))
]
