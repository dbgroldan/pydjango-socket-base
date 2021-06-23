from django.urls import re_path
from customer_socket import consumer

websocket_urlpatterns = [
    re_path(r'ws/customer/(?P<room>\w+)/(?P<user_id>\w+)/$', consumer.Consumer)
]