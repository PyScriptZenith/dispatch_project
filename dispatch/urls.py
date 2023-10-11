from dispatch.apps import DispatchConfig
from django.urls import path

from dispatch.views import DispatchListView

app_name = DispatchConfig.name

urlpatterns = [
    path('', DispatchListView.as_view(), name='dispatch_list'),
]
