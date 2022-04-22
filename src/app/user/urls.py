from django.urls import path

from . import view


app_name = 'user'

urlpatterns = [
    path('api/', view.ShiftList.as_view(), name='shift_list'),
]
