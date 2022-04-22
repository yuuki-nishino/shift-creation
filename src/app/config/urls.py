from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('shirotengu/', include('shirotengu.urls')),
    path('admin/', admin.site.urls),
]
