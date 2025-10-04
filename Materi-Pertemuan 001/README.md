# Network Monitor - Python (Beginner Project)

## Description
This project is a simple **network monitoring tool** built with Python. 
It checks if a host is online, scans specific ports, and logs results to `results.log`.

---

## Features
- Ping multiple IP addresses
- Scan common ports (22, 80, 443)
- Log results with timestamp
- Easy to extend for automation

---

## Files
- `network_monitor.py` → main script
- `config.txt` → list of target IPs/hosts
- `results.log` → output log file
- `README.md` → this instructions file

---

## How to Run
1. Install Python 3.x
2. Put target IPs in `config.txt` (one per line)
3. Run in terminal:
   ```bash
   python network_monitor.py
