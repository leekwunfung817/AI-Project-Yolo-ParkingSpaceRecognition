import win32com.client
import os

qinfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
computer_name = os.getenv('COMPUTERNAME')
qinfo.FormatName="direct=os:"+computer_name+"\\PRIVATE$\\test"
print('qinfo.FormatName',qinfo.FormatName)

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
def send(label,messageContent):
    queue=qinfo.Open(2,0)   # Open a ref to queue
    msg=win32com.client.Dispatch("MSMQ.MSMQMessage")
    msg.Label=label
    msg.Body = messageContent
    msg.Send(queue)
    queue.Close()
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
def receive():
    queue=qinfo.Open(1,0)   # Open a ref to queue to read(1)
    msg=queue.Receive()
    label=msg.Label
    message=msg.Body
    queue.Close()
    return_=(label,message)
    # print('Receive:',return_)
    return return_
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

bytes=bytearray(b'\x06\x01\x02\x08\x03\x01')
print('Send:',bytes)
send("TestMsg",bytes)

(label,message) = receive()
bytes=bytearray(message)
print("Label:",label)
print("Body :",bytes)