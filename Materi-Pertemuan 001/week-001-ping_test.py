# ping_test.py
import os
import platform

# Tentukan target IP atau host
target = "8.8.8.8"  # Google DNS

# Tentukan perintah ping sesuai OS
param = "-n" if platform.system().lower()=="windows" else "-c"

# Jalankan ping
response = os.system(f"ping {param} 4 {target}")

# Cek hasil
if response == 0:
    print(f"{target} is reachable ✅")
else:
    print(f"{target} is not reachable ❌")
