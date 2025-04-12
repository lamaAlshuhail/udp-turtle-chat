import socket
import threading

def print_client_banner():
    GREEN = "\033[92m"
    RESET = "\033[0m"
    print(GREEN + r"""
       _____ _ _            _           
      / ____| (_)          | |           
     | |    | |_  ___ _ __ | |_ 
     | |    | | |/ _ \ '_ \| __|
     | |____| | |  __/ | | | |_ 
      \_____|_|_|\___|_| |_|\__(_)

             UDP CLIENT - by Lama Alshuhail
    ──────────────────────────────────────────────

             ___-------___
         _-~~             ~~-_
      _-~  ||    TURTLE     || ~-_
   /~     ||     CHAT 🐢     ||    ~\
  |_______||_______________||______|
  |_______________________________|
   \_________TURTLE CLIENT________/

     💬 Ready to send & receive messages
""" + RESET)

def receive_messages(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"[Received from {addr}]: {data.decode()}")

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.bind(('0.0.0.0', 0))  # OS picks an available port
    print_client_banner()

    recv_thread = threading.Thread(target=receive_messages, args=(client_socket,), daemon=True)
    recv_thread.start()

    try:
        while True:
            message = input("Enter message to send (or 'exit'): ")
            if message.lower() == 'exit':
                print("Closing client...")
                break
            target_ip = input("Enter server IP: ")
            client_socket.sendto(message.encode(), (target_ip, 12345))
    except KeyboardInterrupt:
        print("\n[Client] Interrupted by user. Exiting.")

if __name__ == "__main__":
    main()
