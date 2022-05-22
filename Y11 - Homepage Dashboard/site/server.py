#!/usr/bin/env python3
import sys
import argparse
from http.server import ThreadingHTTPServer, CGIHTTPRequestHandler

def serve(hostname: str, port: int):
    with ThreadingHTTPServer((hostname, port), CGIHTTPRequestHandler, bind_and_activate=True) as server:
        print(f"🚀 CGI Server Running on http://{result.host or 'localhost'}:{result.port}")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print(f"👋 CGI Server Shutdown")

if __name__ == "__main__":
    parser = argparse.ArgumentParser("CGI Server")
    parser.add_argument("--host", type=str, required=False, default="")
    parser.add_argument("--port", type=int, required=False, default=50081)
    result = parser.parse_args(sys.argv[1:])
    serve(result.host, result.port)
