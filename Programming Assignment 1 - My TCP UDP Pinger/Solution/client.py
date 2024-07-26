import socket

# Creating a client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(("127.0.0.1", 10000))

# Setting a timeout for 1sec
clientSocket.settimeout(1)

# How many request you want to send
N = int(input("Enter the no. of times you want to request: "))

for i in range(N):
    # Requesting a key to server
    request = input("Enter key: ")
    request = request.encode()
    clientSocket.send(request)

    # Getting value for requested key
    response = clientSocket.recv(1024)
    response = response.decode()
    print(f"{response} \n")

clientSocket.close()

