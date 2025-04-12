import socket
import threading

def print_server_banner():
    GREEN = "\033[92m"
    RESET = "\033[0m"
    print(GREEN + r"""
      _____                          
     / ____|                         
    | (___   ___ _ ____   _____ _ __ 
     \___ \ / _ \ '__\ \ / / _ \ '__|
     ____) |  __/ |   \ V /  __/ |   
    |_____/ \___|_|    \_/ \___|_|   

             UDP SERVER - by Lama Alshuhail
    ──────────────────────────────────────────────

             ___-------___
         _-~~             ~~-_
      _-~                    /~-_
   /~  ||        ||        ||    ~\
  |___||________||________||______|
  |________________________________|
   \_______  TURTLE SERVER  ______/

     📡 Listening on 0.0.0.0:12345
""" + RESET)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 12345))
    print_server_banner()

    last_sender = None  # store last client's address

    def receive_messages(sock):
        nonlocal last_sender
        while True:
            data, addr = sock.recvfrom(1024)
            last_sender = addr
            print(f"[Received from {addr}]: {data.decode()}")

    recv_thread = threading.Thread(target=receive_messages, args=(server_socket,), daemon=True)
    recv_thread.start()

    try:
        while True:
            message = input("Enter message to send (or 'exit'): ")
            if message.lower() == 'exit':
                print("Shutting down server...")
                break
            if last_sender:
                server_socket.sendto(message.encode(), last_sender)
            else:
                print("⚠️ No client has contacted the server yet.")
    except KeyboardInterrupt:
        print("\n[Server] Interrupted by user. Exiting.")


if __name__ == "__main__":
    main()
