import sys
from socket import *
def connScan(targetHost, targetPort):
    try:
        # connecting socket with a simple TCP IP connection
        con = socket(AF_INET, SOCK_STREAM)
        con.connect((targetHost, targetPort))
        print('[+]%d/tcp open' % targetPort)
        con.close()
    except:
        print('[-]%d/tcp close' % targetPort)

if __name__ == '__main__':
    n = len(sys.argv)
    if n == 3:
        targetHost = gethostbyname(sys.argv[1])
        targetPort = int(sys.argv[2])
        connScan(targetHost, targetPort)
    else:
        print("Enter the Arguments Properly\n")
        print("Ex: $python3 app.py <targetHost> <targetPort>")