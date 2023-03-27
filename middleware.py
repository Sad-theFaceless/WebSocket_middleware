#!/bin/python3

import sys
import websocket
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

if (len(sys.argv) != 4):
    print("USAGE: " + sys.argv[0] + " $DOMAIN $PORT \"$URL_PATH\"")
    exit(1)

ws_server = "ws://" + sys.argv[1] + ":" + sys.argv[2] + sys.argv[3]

def send_ws(data):
    print("Connecting to " + ws_server)
    ws = websocket.create_connection(ws_server)
    print("Connected.")

    ws.settimeout(5)

    if (data == None):
        ws.close()
        return("No data sent.")
    else:
        print("Sending:\n" + data.decode())
        ws.send(data.decode())
        print("Sent.")
        try:
            resp = ws.recv()
            ws.close()
            return(resp)
        except (TimeoutError, websocket._exceptions.WebSocketTimeoutException):
            ws.close()
            return("No data received.")

def middleware_server(host_port):
    class CustomHandler(SimpleHTTPRequestHandler):
        def do_POST(self) -> None:
            self.send_response(200)
            content_length = int(self.headers['Content-Length'])
            data = self.rfile.read(content_length)
            content = send_ws(data)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(content.encode())
            return

    class _TCPServer(TCPServer):
        allow_reuse_address = True

    httpd = _TCPServer(host_port, CustomHandler)
    httpd.serve_forever()

print("[+] Starting MiddleWare Server")
print("[+] Send POST data to http://127.0.0.1:8081/")

middleware_server(('0.0.0.0',8081))
