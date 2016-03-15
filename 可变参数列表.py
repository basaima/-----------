#def write_multiple_items(file, separator, *args):
  #  file.write(separator.join(args))

'''def fun(*arg):
    print (arg)
    fun(1,2,3)'''

'''
def testFun1(**arg):
    for k in arg.keys():
        print("arg[%s] = %s.", k, arg[k])

def testFun2(*arg1, **arg2):
    print (arg1)
    print (arg2)

if __name__ == '__main__':
    print("How do you do? %d, %d", 2, 3)
    testFun1(One=1, Two=2)
    testFun2(1, 2, 3, One=1, Two=2, Three=3)
    '''

def can(*arg,spe='/'):
    return spe.join(arg)
can('e,','a','d')


def concat(*args, sep="/"):
    print ( sep.join(args))
concat("earth", "mars", "venus")

print ('_'*20)
spe='$$$$$$'
sz=['a','b','c']
print (spe.join(sz))
print ('''line1
         line2''')
print ('\\\\\\\t\\\\\\')
print (r'\\\\\\\t\\\\\\')