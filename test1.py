x = 4

print x

print '######1'

def hello():
  if x == 4 : print 'hello'
  print 'inside block'
print 'outside block'

hello()

print '######2'

from test_module import * 

module_method()
