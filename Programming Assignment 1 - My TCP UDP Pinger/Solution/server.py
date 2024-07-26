import socket

# Creating sever Socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('127.0.0.1', 10000))

# Listening for the connection form client
serverSocket.listen()
clientSocket, address = serverSocket.accept()
print(f"Connection with {address} has been established")

# Dictionary of key value pairs
cache = {
    'key1': 'val1',
    'key2': 'val2',
    'key3': 'val3',
    'key4': 'val4',
}

# Dictionary to keep track for cached keys
cached_keys = {
    'key1': 0,
    'key2': 0,
    'key3': 0,
    'key4': 0
}

keys_requested = 0
keys_cached = 0

try:
    while True:
        # Getting requet form the client
        req_key = clientSocket.recv(1024)
        req_key = req_key.decode()
        
        # if there is no request then breakout form loop
        if not req_key:
            break

        # Counting total no. of keys requested
        keys_requested += 1

        if req_key not in cache.keys():
            msg3 = "Not a valid key".encode()
            clientSocket.send(msg3)

        # if the key is requested more then once
        elif cached_keys[req_key] >= 1:
            msg1 = f"This key has been cached".encode()
            clientSocket.send(msg1)
            cached_keys[req_key] += 1

        # if the keys is not cached then return the value and increment
        elif req_key in cache.keys():
            msg2 = f"Responded value: {cache[req_key]}".encode()
            clientSocket.send(msg2)
            cached_keys[req_key] += 1   

# handling socket errors
except socket.error as e:
    print(e)

finally:
    serverSocket.close()

# Counting how many keys are cached
for v in cached_keys.values():
    if v > 1:
        keys_cached += 1

print(f"Total keys requested: {keys_requested}")
print(f"Total keys Cached: {keys_cached}")