import socket


def main():
    host = '127.0.0.1'
    port = 5006

    s= socket.socket()
    s.connect((host,port))

    message = input("Enter:")
    while message != "exit":
        s.send(message.encode())
        data = s.recv((1024))
        print("Received   :",data.decode())

        message= input("Enter:")
    s.close()
if __name__ == '__main__':
    main()