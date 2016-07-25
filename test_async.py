import threading
import time

class AsyncWrite(threading.Thread):
  def __init__(self, text, out):
    threading.Thread.__init__(self)
    self.text = text
    self.out = out
  
  def run(self):
    f = open(self.out, "a")
    f.write(self.text + '\n')
    f.close()
    print 'Finished Background file write to ' + self.out

def Main():
  message = raw_input('Enter a string to store: ')
  background = AsyncWrite(message, 'out.txt')
  background.start()
  background.join()

Main()
