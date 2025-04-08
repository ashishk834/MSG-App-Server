import socket
import threading

s = socket.socket()
print("Socket has been created.")
s.bind(("localhost",9999))
s.listen(5)
print("Connecting...")

a = []

def rsv(c,add):
    a.append(c)
    print(f"Connected...{add}\n")
    while True:
        try:
            ab = c.recv(1024).decode()
            if not ab:
                print("Disconnected...\n")
                break
            for m in a:
                if m != c:
                    m.send(ab.encode())
        except Exception as e:
            print(f"{e}\n")
    a.remove(c)
    c.close()
while True:
    cc, addr = s.accept()
    threading.Thread(target=rsv, args=(cc, addr), daemon=True).start()