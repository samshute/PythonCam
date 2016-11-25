import cv2
import socket
import pickle
import struct

cap = cv2.VideoCapture(0)
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('localhost',13579))
print 'connect'
while True:
	ret,frame=cap.read()
	data = pickle.dumps(frame)
	clientsocket.sendall(struct.pack("Q", len(data))+data)

