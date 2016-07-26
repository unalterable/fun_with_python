'''
The threading module uses threads, the multiprocessing uses processes. The difference is that threads run in the same memory space, while processes have separate memory. This makes it a bit harder to share objects between processes with multiprocessing. Since threads use the same memory, precautions have to be taken or two threads will write to the same memory at the same time. This is what the global interpreter lock is for.

Spawning processes is a bit slower than spawning threads. Once they are running, there is not much difference.
'''


import os

def child():
    print "We are in the child process with PID= %d"%os.getpid()

def parent():
    print "We are in the parent process with PID= %d"%os.getpid()
    newRef=os.fork()
    if newRef==0:
        child()
    else:
        print "We are in the parent process and our child process has PID= %d"%newRef

parent()
