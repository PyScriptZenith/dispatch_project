from dispatch.apps import DispatchConfig
from django.urls import path
from django.views.decorators.cache import cache_page

from dispatch.views import DispatchListView, DispatchDetailView, DispatchCreateView, DispatchUpdateView, \
    DispatchDeleteView, MessageCreateView, MessageListView, MessageDetailView, MessageUpdateView, MessageDeleteView, \
    IndexView, LogsListView, ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView

app_name = DispatchConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dispatches/', cache_page(60)(DispatchListView.as_view()), name='dispatch_list'),
    path('dispatch/<int:pk>', DispatchDetailView.as_view(), name='dispatch_detail'),
    path('create/', DispatchCreateView.as_view(), name='dispatch_create'),
    path('update/<int:pk>', DispatchUpdateView.as_view(), name='dispatch_update'),
    path('delete/<int:pk>/', DispatchDeleteView.as_view(), name='dispatch_delete'),

    path('messages/', MessageListView.as_view(), name='message_list'),

    path('message/create', MessageCreateView.as_view(), name='message_create'),
    path('message/<int:pk>', MessageDetailView.as_view(), name='message_detail'),

    path('update/message/<int:pk>', MessageUpdateView.as_view(), name='message_update'),
    path('delete/message/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
    path('logs/', LogsListView.as_view(), name='logs_list'),

    path('clients/', ClientListView.as_view(), name='client_list'),
    path('client/<int:pk>', ClientDetailView.as_view(), name='client_detail'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),

]
