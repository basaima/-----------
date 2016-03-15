'''def mya(x):
   # x=int(input(':>'))
    if not isinstance(x,(int,float)):#对参数类型做检查，只允许整数和浮点数类型的参数数据类型检查可以用内置函数isinstance()实现
      raise TypeError('bad op  type')

    #if not isinstance(x, (int, float)):
      # raise TypeError('bad operand type')#
    if x>=0:
        print (x)
        return x
    else:
        print ("-")
        return -x

mya(4.35556)
mya(-9)'''


import  math
def quadratic(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError("bad operand type")
    y=b*b-4*a*c
    if b*b-4*a*c>=0:
       print ('Y')
       x1=(-b+math.sqrt(y))/(2*a)
       x2=(-b-math.sqrt(y))/(2*a)
       print(x1,x2)
       return x1,x2
    else :
        print ("无解")
quadratic(1,8,3)
quadratic(2,2,4)
