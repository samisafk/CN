import socket

def port_scan():
    link = input("Enter link to perform scan ports on: ")
    host = socket.gethostbyname(link)
    res = "a"
    
    while res != "bye":
        min_port = int(input("Enter the lowest limit of range: "))
        max_port = int(input("Enter the highest limit of range: "))
        
        for port in range(min_port, max_port + 1):
            try:
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                print(f"Trying connection to {host} on port {port}......")
                
                if client_socket.connect_ex((host, port)) == 0:
                    print(f"Connection to {host} on port {port} was SUCCESSFUL")
                else:
                    print(f"Connection to {host} on port {port} was A FAILURE")
            except socket.error as e:
                print(f"Error connecting to {host} on port {port}: {e}")
            finally:
                client_socket.close()

        res = input("Scan has ended. To Exit press 'bye'. To continue search with different inputs press 'y': ").lower()
    
    print("Scanner Exited")

if __name__ == "__main__":
    port_scan()
