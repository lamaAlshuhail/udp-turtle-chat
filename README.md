# 🐢 UDP Turtle Chat

<img width="642" alt="Screenshot 2025-04-12 at 2 10 55 PM" src="https://github.com/user-attachments/assets/4a2f9453-b4da-43ad-a63a-258bb5732324" />

<img width="583" alt="Screenshot 2025-04-12 at 2 11 36 PM" src="https://github.com/user-attachments/assets/a7065f57-47aa-4c4b-bd70-72cd33d93b60" />

A simple Python program demonstrating UDP-based communication between a client and server using sockets and threading — with a fun twist: turtle ASCII art banners! 🐢✨

## Features

- UDP communication using `socket`, `sendto()`, and `recvfrom()`
- Bi-directional messaging (Client ↔ Server)
- Uses `Thread()` for receiving while sending
- Auto-reply to last sender on the server side
- ASCII turtle banners 🐢
- Created by Lama Alshuhail for a Programming for Cybersecurity lab assignment

---

## Project Files

- `UDP_Client.py` – the turtle-themed UDP client
- `UDP_Server.py` – the turtle-themed UDP server

---

## How to Run

### 1. Start the server

```bash
python3 UDP_Server.py
```

2. Start the client (in a new terminal)
```bash
python3 UDP_Client.py
```

3. Send messages
From client to server: enter the message and server IP (127.0.0.1 if local)

From server to client: just type a reply — no need to enter IP


## Technical Notes

- `0.0.0.0` is used in `bind()` to allow listening on all interfaces.
- For sending, always use:
  - `127.0.0.1` if client and server are on the **same machine**
  - Your actual local IP (e.g., `192.168.x.x`) for **LAN communication**
- The client is assigned a random available port using `bind(('0.0.0.0', 0))`.
- The server automatically replies to the **last known sender** without retyping the IP.

