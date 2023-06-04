import socket

IP = "127.0.0.1"  # localhost
PORT = 7000
SIZE = 1024

socketServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketServer.bind((IP, PORT))
print('begin write image file "receive_img.jpeg"')
with open('receive_img.jpeg', 'wb') as image:   # 開始寫入圖片檔
    while True:
        imgData = socketServer.recv(SIZE)# 接收遠端主機傳來的數據
        if not imgData:
            break  # 讀完檔案結束迴圈
        image.write(imgData)
    image.close()
    print('image save')
socketServer.close()
