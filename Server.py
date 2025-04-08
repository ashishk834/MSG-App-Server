import socket
import threading
import os

PORT = int(os.environ.get("PORT", 9999))  # default to 9999 for local
s = socket.socket()
s.bind(("0.0.0.0", PORT))
s.listen(5)

print(f"Server running on port {PORT}...")

clients = []

def rsv(c, addr):
    clients.append(c)
    print(f"Connected...{addr}")
    while True:
        try:
            msg = c.recv(1024).decode()
            if not msg:
                break
            for client in clients:
                if client != c:
                    client.send(msg.encode())
        except Exception as e:
            print(e)
            break
    clients.remove(c)
    c.close()

while True:
    conn, addr = s.accept()
    threading.Thread(target=rsv, args=(conn, addr), daemon=True).start()
