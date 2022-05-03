from websocket import create_connection
import json

ws = create_connection("ws://38.130.130.45:8000/ws/chat/hi/")
print(ws.recv())
print("Sending 'Hello, World'...")
ws.send(json.dumps({
'message': {"latitude":51.50772530994978,"longitude":-0.12848742222899778},
'command':'veregood_get_services',
}))
print("Sent")
print("Receiving...")
result =  ws.recv()
print("Received '%s'" % result)
ws.close()