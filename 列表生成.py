print (list(range(0,9)))

l=[]
for i in range(1,12):
    l.append(i*i)
print (l)

print ([i*i for i in range(1,13)])#多写几次

print ([m+n for m in 'ABC' for n in "XYZ"])#生成全排列的方法
print ([m+n+y for m in 'ABC' for n in "XYZ" for y in '123'])

import  os
print([d for d in os.listdir('.')])#列出当前目录下的所有文件和目录名

g= {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in g.items():
    print (k,'=',v)
print ("_______+++++++++")
print ([k+'='+v for k,v in g.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print ([s.lower() for s in L])

f=[]
for i in L:######????????????????????
   i.lower()
   print (f.append(i))

k='DFFFFF'
print (k.lower())

L1 = ['Hello', 'World', 18, 'Apple', None]
print ([g1.lower()for g1 in L1 if isinstance(g1,str)==True])