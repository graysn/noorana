import os, http.server, socketserver

os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = 3000
Handler = http.server.SimpleHTTPRequestHandler
Handler.log_message = lambda self, fmt, *args: print(fmt % args)
with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print(f'Serving noorana-feedback at http://localhost:{PORT}')
    httpd.serve_forever()
