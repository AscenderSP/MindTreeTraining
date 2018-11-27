import socket

def main():
    host = '127.0.0.1'
    port= 5006

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)
    c, addr = s.accept()
    print("Connection Build from  :",str(addr))
    while True:
        data  = c.recv(1024).decode()
        if not data:
            break
        print("received data :",str(data))
        data=str(data).upper()
        print("Sending...",str(data))
        c.send(data.encode())
    c.close()
if __name__ == '__main__':
    main()