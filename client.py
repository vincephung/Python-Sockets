import time
import socket

try:
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[C]: Client socket created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()
    
# Define the port on which you want to connect to the server
port = 50008
localhost_addr = socket.gethostbyname(socket.gethostname())

# connect to the server on local machine
server_binding = (localhost_addr, port)
cs.connect(server_binding)

# open file and read
input = open("in-proj0.txt")
output = open("out-proj0.txt","w")

fileLines = input.readlines()
for line in fileLines:
    if line:
        # handle edge case when the last line in the input does not end with newline
        if '\n' not in line:
            line += '\n'

        print("Input : %s" %line, end='')
        cs.send(line.encode("utf-8"))
    
        curLine = ""
        while True:
            data_from_server = cs.recv(1024).decode('utf-8')
            if data_from_server:
                curLine += data_from_server
                if '\n' in data_from_server:
                    output.write(curLine)
                    print("Output: %s" %curLine)
                    curLine = ""
                    break                
            else:
                break

#close file
input.close()
output.close()

# close the client socket
cs.close()
exit()