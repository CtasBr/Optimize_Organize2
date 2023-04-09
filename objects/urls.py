from django.urls import path

from .views import *

urlpatterns = [
    path('dashboard/<str:item>', dashboard, name='dashboard'),
    path('registry/', registry, name='registry'),
    path('object/<int:object_id>/', view_object, name='view_obj'),
    path('', index)
]