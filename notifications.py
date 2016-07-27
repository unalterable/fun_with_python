import subprocess
from os import system

def sendmessage(message, title='Notification: '):
  # subprocess.Popen(['notify-send', message])
  system('notify-send "'+title+'" "'+message+'"')
  
  return

if __name__ == '__main__':
  sendmessage('hello')

