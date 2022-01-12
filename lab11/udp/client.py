from socket import *
serverName = "127.0.0.1"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
name= input("\nEnter file name: ")
word = input("\nenter word: ")
sentence=[name,word]
sentence=str(sentence)
#sentence=sentence.encode()
clientSocket.sendto(bytes(sentence,"utf-8"),(serverName, serverPort))
filecontents,serverAddress = clientSocket.recvfrom(2048)
print ("\nReply from Server:\n")
print (filecontents.decode("utf-8"))
# for i in filecontents:
# print(str(i), end = &#39;&#39;)
clientSocket.close()
clientSocket.close()
