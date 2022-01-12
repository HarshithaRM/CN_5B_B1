from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("127.0.0.1", serverPort))
print ("The server is ready to receive")
while 1:
  sentence, clientAddress = serverSocket.recvfrom(2048)
  sentence = sentence.decode("utf-8")
  sentence=eval(sentence)

  name= sentence[0]
  word = sentence[1]
  file=open(name,"r")
  l=file.read(2048)
  l=l.split()
  count=0
  
  for w in l:
    if w == word:
      count+=1
  
  
  serverSocket.sendto(bytes(f"{word} is present in file {count} many times","utf-8"),clientAddress)
  print ("\nSent contents of ", end = " ")
  print (sentence)
# for i in sentence:
# print (str(i), end = &#39;&#39;)
file.close()
