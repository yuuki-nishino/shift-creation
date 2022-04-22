from django.urls import path

from . import views


app_name = 'shirotengu'

urlpatterns = [
    path('api_shift/', views.ShiftList.as_view(), name='shift_list'),
    path('api_user/', views.UserList.as_view(), name='user_list'),
    path('api_store/', views.StoreList.as_view(), name='store_list'),
]