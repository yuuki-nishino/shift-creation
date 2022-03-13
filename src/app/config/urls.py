from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('login/', include('login.urls')),
    path('user/', include('user.urls')),
    path('manager/', include('manager.urls')),
    path('admin/', admin.site.urls),
]
