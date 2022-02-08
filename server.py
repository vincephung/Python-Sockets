import time
import socket

# Reverse string and append original
def reverseAppend(string):
    reverseLine = "".join(reversed(string))
    newLine = reverseLine + string
    return newLine

try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[S]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ('', 50008)
ss.bind(server_binding)
ss.listen(1)

host = socket.gethostname()
print("[S]: Server host name is {}".format(host))
localhost_ip = (socket.gethostbyname(host))
print("[S]: Server IP address is {}".format(localhost_ip))
csockid, addr = ss.accept()
print ("[S]: Got a connection request from a client at {}".format(addr))


curLine = ""
while True:
    data = csockid.recv(1024).decode('utf-8')
    if data:
        curLine += data
        if '\n' in data:
            # If there is a new line, remove it so that when you reverse the string, the new line doesnt get added to the front
            newLine = reverseAppend(curLine[:-1]) + '\n'
            #print("[S]: %s" %newLine)
            csockid.send(newLine.encode('utf-8'))
            curLine = ""
    else:
        break
        
# Close the server socket
ss.close()
exit()

