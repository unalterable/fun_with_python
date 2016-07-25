x = 4

print x

print '######1'

def hello():
  if x == 4 : print 'hello'
  print 'inside block'
print 'outside block'

hello()

print '######2'

import test_module

print '######3'

a = test_module.module_method()

print '######4'

print a #this is nothing as #module_method() returns nothing

print '######5'

a = test_module.module_method

print '######6'

a()
