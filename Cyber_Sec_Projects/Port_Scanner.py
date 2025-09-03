'''
This is my port scanner where ports will try to be connected to see if the port is
open or closed. The user is able to choose a hostname and which ports to check.
The output will display the ports and if they are open or closed.



'''
import socket

print("Welcome to my port scanner. ")

def user_specifics():
    common = [20, 21, 22, 23, 25, 53, 80, 443]
    while True:
        ip = input("PLease enter the hostname or IP address: ")
        port = input("Please enter a port or range or ports (i.e 20-1024), " +
                    "\nor if you would like, type 'common' to check common ports, \nor " +
                    "type 'all' to check all available ports: ")
        ip = socket.gethostbyname(ip) #converts hostname to IP
        if port.strip().lower() == "all":
            print("all")
        elif port.strip().lower() == "common":
            print("common")
            
        port = port.strip().split("-")
        try:
            port = list(map(int, port))
        except ValueError:
            print("Please enter a valid port or range of ports. ")
            continue
                    
                        
        return ip, port

def connect_port(ip, port):
    while True:
        s = socket.socket()
    
    

    
    
    
    
    
    
    
while True:
    ip, port = user_specifics()
    connect_port(ip, port)