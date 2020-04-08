from channels.routing import ProtocolTypeRouter
# from handleRequest.consumers import ws_connect, ws_disconnect

application = ProtocolTypeRouter({
    # (http->django views is added by default)
})
# channel_routing = [
#     route('websocket.connect', ws_connect()),
#     route('websocket.disconnect', ws_disconnect())
# ]