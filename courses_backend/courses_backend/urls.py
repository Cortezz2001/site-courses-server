
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/projects/', include("project.urls")),
    path('admin/', admin.site.urls),
]
