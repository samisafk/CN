import socket

def dns_lookup():
    print("DNS Lookup")
    link = ""
    while link != "end":
        link = input("Enter website name (type 'end' to stop): ").strip()  # Remove any extra spaces
        if link == "end":
            break
        try:
            host = socket.gethostbyname(link)
            print(f"IP address of {link} is {host}\n")
        except socket.gaierror:
            print(f"DNS lookup failed for {link}. Please enter a valid website name.")

    print("Closed.")

dns_lookup()
