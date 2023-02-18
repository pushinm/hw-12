from django.urls import path
from .views import all_users, double_filter_man, double_filter_woman

urlpatterns = [
    path('', all_users, name='all_users'),
    path('man/', double_filter_man, name='double_filter_man'),
    path('woman/', double_filter_woman, name='double_filter_woman'),
]