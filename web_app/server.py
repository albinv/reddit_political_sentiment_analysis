import http.server
import socketserver

PORT = 7100
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Server started at localhost:" + str(PORT))
    httpd.serve_forever()