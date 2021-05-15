import socket

target_host = 'google.com'
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
client.send(b'GET \/HTPP 1.1\n\rHost: google.com \r\n\r\n')

# receive some data
response = client.recv(4096)

print(response)
client.close()

