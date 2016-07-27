from notifications import sendmessage
import time

for i in range(10,20):
  string = 'hello %s' % i
  print string
  sendmessage(string) 
  time.sleep(1)
