from channels.auth  import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import customer_socket.routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            customer_socket.routing.websocket_urlpatterns
        )
    )
})



