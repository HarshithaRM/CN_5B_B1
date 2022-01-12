from socket import *

files=['abc.txt','abc1.txt','hello.txt','hello1.txt']

serverName="127.0.0.1"
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)
while 1:
  print (" The server is ready to receive")
  res=" "

  connectionSocket, addr = serverSocket.accept()
  sentence = connectionSocket.recv(1024).decode()
  for name in files:
    print(name)
    file=open(name,"r")
    l=file.read(1024)

    
    if sentence in l:
        print(l)
        res=res+" "
        res+=name
    file.close()


  connectionSocket.send(bytes(res,"utf-8"))
  print ("\nSent contents of "+ res)
  connectionSocket.close()
