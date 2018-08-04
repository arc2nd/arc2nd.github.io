import os
import BaseHTTPServer
import CGIHTTPServer

serverAddr = ("", 8000)
serv = BaseHTTPServer.HTTPServer(serverAddr, CGIHTTPServer.CGIHTTPRequestHandler)
serv.serve_forever()


