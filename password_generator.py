import socket

target = input("Enter IP: ")

for port in range(1, 100):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is open")

    s.close()
