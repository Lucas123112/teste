import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = "/home/ubuntu/codi_mes_presentation"

os.chdir(DIRECTORY)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"serving at port {PORT}")
    httpd.serve_forever()

