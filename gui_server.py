#!/usr/bin/env python3
"""
Interactive GUI Server for Dr. Çiğdem Avcı's Research Lab.
Serves the flagship interactive research demonstrator on localhost.
Zero external dependencies (pure Python 3 standard library).
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

PORT = 8080
GUI_DIR = (Path(__file__).resolve().parent / "gui") if (Path(__file__).resolve().parent / "gui").is_dir() else Path(__file__).resolve().parent

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(GUI_DIR), **kwargs)
        
    def log_message(self, format, *args):
        # Clean terminal output
        pass

def main():
    os.chdir(GUI_DIR)
    # Check port availability or find next available
    port = PORT
    server = None
    for p in range(PORT, PORT + 20):
        try:
            server = socketserver.TCPServer(("", p), Handler)
            port = p
            break
        except OSError:
            continue
            
    if not server:
        print("[!] Error: Could not bind to any port between 8080 and 8100.")
        sys.exit(1)
        
    url = f"http://localhost:{port}"
    print("=" * 72)
    print(" DR. ÇİĞDEM AVCI RESEARCH LAB — INTERACTIVE GUI SERVER")
    print("=" * 72)
    print(f"[✓] Server running successfully at: {url}")
    print(f"[✓] Serving directory: {GUI_DIR}")
    print("[*] Demonstrators Available:")
    print("    1. Emotional Gossip Protocol (ECAGP Multi-Agent P2P Simulator)")
    print("    2. Explainable Cybersecurity (6G O-RAN Closed-Loop EAL Engine)")
    print("    3. ClinAssure (Liver Transplant AI Meta-Assurance Governance)")
    print("-" * 72)
    print("Press Ctrl+C to stop the server.")
    print("=" * 72)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Server stopped cleanly.")
        server.server_close()

if __name__ == "__main__":
    main()
