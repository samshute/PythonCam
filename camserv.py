import cv2
import socket
import pickle
import struct

Host = ''
Port = 13579

cv2.namedWindow("preview")
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket Created'

soc.bind((Host,Port))
print 'Socket bind complete'
soc.listen(10)
print 'Socket now listening'

conn,addr = soc.accept()

print 'received connection'
data = ""
payload_size = struct.calcsize("Q")
while True:
	while len(data) < payload_size:
		data=conn.recv(4096)
	packed_msg_size = data[:payload_size]
	data = data[payload_size:]
	msg_size = struct.unpack("Q", packed_msg_size)[0]
	while len(data) < msg_size:
		data += conn.recv(4096)
	frame_data = data[:msg_size]
	data = data[msg_size:]
	frame=pickle.loads(frame_data)
	print frame.size
	cv2.imshow("preview", frame)
	key = cv2.waitKey(10)
	if(key == 27):
		break
