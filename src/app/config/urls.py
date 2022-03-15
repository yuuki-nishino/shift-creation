from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('login/', include('shift.app.login.urls')),
    path('user/', include('shift.app.user.urls')),
    path('manager/', include('shift.app.manager.urls')),
    path('admin/', admin.site.urls),
]
