import socket
hostname = "google.com"
ip_address = socket.gethostbyname(hostname)

print(f"Ip {hostname}: {ip_address}")