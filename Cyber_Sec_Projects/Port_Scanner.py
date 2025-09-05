'''
This is my port scanner where you enter the hostname or IP address, then 
you can choose which ports you want to to try to connect to, including every port and common ports. Then the system
will scan every port that was selected and output which ports are open.



'''
import socket
import concurrent.futures
import threading
from tqdm import tqdm
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
        try:
            if int(port) < 0 or int(port) > 65535:
                print("Please enter a valid port. ")
                continue
        except ValueError:
            pass
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
        with lock:
            open_ports.append(portnum)
    except socket.timeout:
        pass
    except ConnectionRefusedError:
        pass
    finally:
        sock.close()
    
         

def connect_port(ip, port):
    big_scan_threshold = 1000
    common = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3389, 8080]
    if port == "all":
        port_range = range(0,65535)
        print("Trying to connect to all ports")
        executor = concurrent.futures.ThreadPoolExecutor(max_workers = 1000)
        futures = [executor.submit(big_scan, ip, portnum) for portnum in port_range]
        for _ in tqdm(concurrent.futures.as_completed(futures), total = len(futures)):
            pass
        executor.shutdown(wait = True)
        print("Open ports:", ", ".join(map(str, open_ports)))
        open_ports.clear()
        
    elif port == "common":
        print("Trying to connect to common ports ")
        executor = concurrent.futures.ThreadPoolExecutor(max_workers = 50)
        for portnum in common:
            executor.submit(single_scan_port, ip, portnum)
        executor.shutdown(wait = True)  
        
    else:
        executor = concurrent.futures.ThreadPoolExecutor(max_workers = 100)
        
        if len(port) == 1:
            executor.submit(single_scan_port, ip, port[0])
            
        else:
            port_range = range(port[0], port[-1]+1)
            if len(port_range) > big_scan_threshold: #decides if we do normal or big scan
                futures = [executor.submit(big_scan, ip, portnum) for portnum in port_range]
                for _ in tqdm(concurrent.futures.as_completed(futures), total = len(futures)):
                    pass
                
                print("Open ports:", ", ".join(map(str, open_ports)))
                open_ports.clear()   
            else:
                futures = [executor.submit(single_scan_port, ip, portnum) for portnum in port_range]
                for _ in tqdm(concurrent.futures.as_completed(futures), total = len(futures)):
                    pass
                
        executor.shutdown(wait = True)
            
    
    
while True:
    ip, port = user_specifics()
    connect_port(ip, port)