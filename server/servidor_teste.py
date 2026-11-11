import http.server
import socketserver

PORTA = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORTA), Handler) as httpd:
    print(f"Servidor rodando na porta {PORTA}")
    httpd.serve_forever()   