class StringManipulation:

  def append1(self, string1, string2):
    return string1 + string2


if __name__ == '__main__':
  
  from notifications import sendmessage
  import time
  strings = {}
  
  strings[1] = StringManipulation().append1('app-', '-end')
  strings[2] = StringManipulation().append1('tried ', strings[1])
   
  
  for key, string in strings.iteritems():
    print string
    sendmessage(string) 
    time.sleep(5)
