import socket

 

msg         = "Datagram from client";

ipAndPort   = ("127.0.0.1", 8080);

udpClient   = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);

 

# Send a datagram to the UDP server

udpClient.sendto(msg.encode(), ipAndPort);

 

# Receive a reply from UDP server

datagramFromServer  = udpClient.recv(1024);

 

# Print the received datagram from server

print(datagramFromServer.decode());