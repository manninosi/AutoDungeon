import socket, time, sys

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 8080#default free point

#Bind the host and port

new_socket.bind((host_name, port))

print("Binding Successfull!")
print("This is your ip: ", s_ip)


#Listening for connections
name = input("Enter your nickname: ")
new_socket.listen(1)


#Accepting incoming connections
conn, add = new_socket.accept()
	#Conn - connection to the socket
	#Add - IP address of the client


print("Recieved connection from ", add[0])
print("Connection Established. Connected from : ", add[0])