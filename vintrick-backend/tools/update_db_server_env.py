import socket
import os
import time

ENV_PATH = ".env"
SUBNET = "100.64.1."  # Adjust as needed
PORT = 1433
TIMEOUT = 0.5  # seconds

def scan_sql_servers():
    found_ips = []
    for last_octet in range(1, 255):
        ip = f"{SUBNET}{last_octet}"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(TIMEOUT)
        try:
            s.connect((ip, PORT))
            found_ips.append(ip)
            print(f"Found SQL Server on {ip}")
        except Exception:
            pass
        finally:
            s.close()
    return found_ips

def update_env_db_server(new_ip):
    updated = False
    lines = []
    with open(ENV_PATH, "r") as f:
        for line in f:
            if line.startswith("DB_SERVER="):
                lines.append(f"DB_SERVER={new_ip},{PORT}\n")
                updated = True
            else:
                lines.append(line)
    if not updated:
        # Add the line if not present
        lines.append(f"DB_SERVER={new_ip},{PORT}\n")
    with open(ENV_PATH, "w") as f:
        f.writelines(lines)
    print(f".env updated: DB_SERVER={new_ip},{PORT}")

if __name__ == "__main__":
    print("Scanning for SQL Servers on subnet...")
    ips = scan_sql_servers()
    if not ips:
        print("No SQL Servers found on this subnet.")
    else:
        # Use the first found IP
        new_ip = ips[0]
        last_octet = new_ip.split('.')[-1]
        print(f"Using {new_ip} (last octet: {last_octet}) for DB_SERVER")
        update_env_db_server(new_ip)