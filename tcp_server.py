import socket

IP = "127.0.0.1"  # localhost
PORT = 6000
SIZE = 1024

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.bind((IP, PORT))
tcpServer.listen(True)

print("Initialize Success")

ClientSocket, ClientAddress = tcpServer.accept()

print('Connect Success')

with open('receive_img.jpeg', 'wb') as image:  # 開始寫入圖片檔
    while True:
        imgData = ClientSocket.recv(SIZE)  # 接收遠端主機傳來的數據
        if not imgData:
            break  # 讀完檔案結束迴圈
        image.write(imgData)
    image.close()
    print('image save')
tcpServer.close()
