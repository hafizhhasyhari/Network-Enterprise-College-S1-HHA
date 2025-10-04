# network_monitor.py
import socket
import os
import platform
from datetime import datetime

# Load targets from config
with open("config.txt") as f:
    targets = [line.strip() for line in f if line.strip()]

# Function ping
def ping_host(host):
    param = "-n" if platform.system().lower()=="windows" else "-c"
    response = os.system(f"ping {param} 2 {host} >nul 2>&1")
    return response == 0

# Function check port
def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

# Log results
with open("results.log", "a") as log:
    log.write(f"\n--- Network Monitor Run {datetime.now()} ---\n")
    for target in targets:
        status = "Online ✅" if ping_host(target) else "Offline ❌"
        log.write(f"{target}: {status}\n")
        print(f"{target}: {status}")
        # Port check
        for port in [22, 80, 443]:
            port_status = "open ✅" if check_port(target, port) else "closed ❌"
            log.write(f"  Port {port}: {port_status}\n")
            print(f"  Port {port}: {port_status}")

# Author : @hafizhhasyhari
# HHA
# Indonesia
# gks
