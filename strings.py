from notifications import sendmessage
import time

strings = {}

strings[1] = 'hello %s' % 5
strings[2] = 'hello %s' % 5
strings[3] = 'hello %s' % 5
strings[4] = 'hello %s' % 5

for key, string in strings.iteritems():
  print string
  sendmessage(string) 
  time.sleep(5)
