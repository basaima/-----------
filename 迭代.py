d = {'a': 1, 'b': 2, 'c': 3}
for i in d.items():
    print (i)

from collections import  Iterable#如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
print (isinstance('abc',Iterable))

for i,value in enumerate(['a','b','c']):
    print (i,value)
    print ("++++++++++++++++++++++++")
for x,y in [(1,2),(3,3),(5,7),(3,1)]:
    print (x,y)