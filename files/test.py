testfile1 = 'test1.txt'
testtext1 = 'hello testfile1'


# creating a test file
print '1: try to create file'
f1 = open(testfile1, 'w')
f1.write(testtext1)
print '1: done'
print


# try to read the file without closing
print '2: read and print file contents (without closing)'
f2 = open(testfile1, 'r')
print f2.read()
print '2: done'
print


# close and try to read again
print '3: close and try again'
f1.close()
f2.close()

f3 = open(testfile1, 'r')
print f3.read()
print '3: done'
print

# delete file
print '4: delete file'
import os
os.remove(testfile1)
print "File Removed!"
print 'done'
print
