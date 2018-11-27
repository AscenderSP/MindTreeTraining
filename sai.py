import socket,threading
from tkinter import *
socketObj = socket.socket()

def connect():
    ipAddress = ipAndPortFromGUI.get().split(":")[0]
    port = ipAndPortFromGUI.get().split(":")[1]
    print("IP = ",ipAddress," port = ",port)
    socketObj.connect((ipAddress,10500))

    def sendP2PMessage():
        while True:
            message = str(input("Enter message to send"))
            socketObj.send(message.encode("UTF-8"))

    def receiveP2PMessage():
        while True:
            message = socketObj.recv(1024)
            print(message.decode("UTF-8"))

    threading.Thread(target=sendP2PMessage).start()
    receiveP2PMessage()
def receive():
    socketObj.bind(('', 10500))
    socketObj.listen(2)
    print("Waiting for connection \n")
    c, addr = socketObj.accept()
    print("Got connection from "+str(addr))
    def sendP2PMessage():
        while True:
            message = str(input("Enter message to send"))
            c.send(message.encode("UTF-8"))

    def receiveP2PMessage():
        while True:
            message = c.recv(1024)
            print(message.decode("UTF-8"))

    threading.Thread(target=sendP2PMessage).start()
    receiveP2PMessage()
threading.Thread(target=receive).start()
window = Tk()
window.title("P2P Chat")
myIP = str(socket.gethostbyname(socket.gethostname()))
var = "Ask your friend to connect to "+myIP+":10500 or \n enter your friends IP below and press on Connect button"
label = Label(window, text=var).pack()
ipAndPortFromGUI = StringVar()
entryBoxUsername = Entry(window, textvariable=ipAndPortFromGUI).pack()
button = Button(window, width=8, height=1, text="Connect", command=connect, font=('Comic Sans MS', 14, 'bold'),
                relief=RAISED, )
button.pack()
window.mainloop()