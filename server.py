# Echo server program
import socket
import subprocess

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
while 1:
    conn, addr = s.accept()
    print 'Connected by', addr
    
    subprocess.call(["sh", "traffic_gen.sh"])
    
    conn.sendall("Traffic Generation on " + str(socket.gethostname()) + "Finished")
    conn.close()
