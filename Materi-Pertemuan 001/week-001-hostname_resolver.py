# hostname_resolver.py
import socket

host = "8.8.8.8"  # Bisa diganti dengan IP lain

try:
    hostname = socket.gethostbyaddr(host)
    print(f"IP {host} resolves to hostname: {hostname[0]}")
except socket.herror:
    print(f"Cannot resolve hostname for IP {host}")
