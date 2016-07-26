'''
The threading module uses threads, the multiprocessing uses processes. The difference is that threads run in the same memory space, while processes have separate memory. This makes it a bit harder to share objects between processes with multiprocessing. Since threads use the same memory, precautions have to be taken or two threads will write to the same memory at the same time. This is what the global interpreter lock is for.

Spawning processes is a bit slower than spawning threads. Once they are running, there is not much difference.
'''


import os
import time


def parent(parent_delay):
    print "We are in the parent process with PID= %d"%os.getpid()
    newRef=os.fork()
    '''
    When you call os.fork, you create a new process that is an exact copy of the existing process except that in the original process, fork returns the process ID of the new (child) process, and in the new process, fork returns 0. This difference is how you can do something different in the parent and in the child.
    '''
    print newRef
    if newRef==0:
      pid = os.getpid()
      print "We are in the child process with PID= %d"%pid
    else:
      time.sleep(parent_delay)
      print "We are in the parent process and our child process has PID= %d"%newRef

parent(0.1)
