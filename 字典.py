d={'a':56,'b':90,'c':67,'e':78}
print (d['a'])
d['f']=88
print (d)
print ('y'in d)
print (d.get('T'))
d.pop('b')
print (d)
################set#######################
s=set([1,2,3,4,5,6])
print (s)
s=set([11,2,3,3,3,4,5,6,6])
print (s)
s.add(9)
print (s)
s.remove(3)
print (s)

a=[1,2,3,56,5,4,3]

print(a.sort())#为何不能用这种方式？？？？？？？
x = [4, 6, 2, 1, 7, 9]
x.sort()
print (x) # [1, 2, 4, 6, 7, 9]
y='abc'
b=y.replace('a','D')
print (b)
print (y)