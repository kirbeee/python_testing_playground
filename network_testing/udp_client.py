import socket
IP = "127.0.0.1"  # localhost
PORT = 7000
IMG_PATH = "testing_img.jpeg"
SIZE = 1024

socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketClient.connect((IP, PORT))

print("server start at -> ", IP, ":", PORT, sep="")

with open(IMG_PATH, "rb") as image:
    while True:
        imgData = image.readline(SIZE)
        if not imgData:
            break  # 讀完檔案結束迴圈
        socketClient.send(imgData)
    socketClient.close()
