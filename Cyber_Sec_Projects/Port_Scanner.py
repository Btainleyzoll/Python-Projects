'''
This is my port scanner where ports will try to be connected to see if the port is
open or closed. The user is able to choose a hostname and which ports to check.
The output will display the ports and if they are open or closed.



'''
import socket
import concurrent.futures
import threading
print("Welcome to my port scanner. ")
lock = threading.Lock()
def user_specifics():
    
    while True:
        ip = input("PLease enter the hostname or IP address: ")
        port = input("Please enter a port or range or ports (i.e 20-1024), " +
                    "\nor if you would like, type 'common' to check common ports, \nor " +
                    "type 'all' to check all available ports: ")
        try:
            ip = socket.gethostbyname(ip) #converts hostname to IP
        except socket.gaierror: #makes sure the hostname is valid
            print("Please enter a valid hostname or IP")
            continue
        
        if port.strip().lower() == "all":
            print("Will try to connect to every port 0-65535. ")
            return ip, port
        elif port.strip().lower() == "common":
            print("Will try all the common ports, (21, 22, 23, 25, 53, 80 110, 143, 443, 3389)")
            return ip, port
        port = port.strip().split("-")
        try:
            port = list(map(int, port))
        except ValueError:
            print("Please enter a valid port or range of ports. ")
            continue
                    
                        
        return ip, port

def single_scan_port(ip, portnum):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(.5)
    try:
        sock.connect((ip, portnum))
        with lock:
            print(f"Port {portnum} = Open")
    except socket.timeout:
        with lock:
            print(f"Port {portnum} = Connection Timed out")
    except ConnectionRefusedError:
        with lock:
            print(f"Port {portnum} = Closed")
    finally:
        sock.close()
open_ports = []


def big_scan(ip, portnum):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(.5)
    try:
        sock.connect((ip, portnum))
        open_ports.append(portnum)
    except socket.timeout:
        pass
    except ConnectionRefusedError:
        pass
    finally:
        sock.close()
    
         

def connect_port(ip, port):
    common = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3389, 8080]
    if port == "all":
        print("Trying to connect to all ports")
        executor = concurrent.futures.ThreadPoolExecutor(max_workers = 50)
        for portnum in range(0, 1500):
            executor.submit(big_scan, ip, portnum)
        executor.shutdown(wait = True)
        print("Summary: \n" +
              f"List of open ports {open_ports}\n" +
              "All other ports closed or connection timed out.\n")
        open_ports.clear()
    elif port == "common":
        print("Trying to connect to common ports ")
        executor = concurrent.futures.ThreadPoolExecutor(max_workers = 50)
        for portnum in common:
            executor.submit(single_scan_port, ip, portnum)
        executor.shutdown(wait = True)  
    else:
        executor = concurrent.futures.ThreadPoolExecutor(max_workers = 50)
        
        if len(port) == 1:
            executor.submit(single_scan_port, ip, port[0])
        else:
            for portnum in range(port[0], port[-1]):
                if range(port[0], port[-1]) > 1000:
                    executor.submit(big_scan, ip, portnum)
                    print("Summary: \n" +
                    f"List of open ports {open_ports}\n" +
                    "All other ports closed or connection timed out.\n")
                    open_ports.clear()
                else:
                    executor.submit(single_scan_port, ip, portnum)
        executor.shutdown(wait = True)
            
    
    
while True:
    ip, port = user_specifics()
    connect_port(ip, port)