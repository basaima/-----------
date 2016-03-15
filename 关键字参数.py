'''
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')
parrot()
'''
'''
def p(a,b='ss',c='cc',d='ww'):
    print ('sss',c,d)
    print ('qwer',a,'asdf')
    print ('________o,omg',d)
    print ("--+++++ahs,")


p(90)
p(a=1000)
p(a=1000,b='sdf')'''

'''def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           dd="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")#如果一个函数定义中的最后一个形参有 ** （双星号）前缀,所有正常形参之外的其他的关键字参数都将被放置在一个字典中传递给函数

'''



def canshu(k,k1,*k2,**k3):
    print ('这首歌','给我',k1)
    print ('这世界','的',k)
    for i in k2:#i 将从第一个元素开始依次接收每个元素的值
       print (i)
    print ('=='*30)
    for j in k3:
        print (j)
    print ('++'*30)
    ke=sorted(k3.keys())#对字典里的关键字进行了排序关键字有wangyun，yiyang，wangjunkai
    for kw in ke:
        print (kw ,':',k3[kw])

canshu('快乐','太阳','Doyouloveme',
        wangyuan='wy',yiyang='^yy^',wangjunkai='wjk')#wy，yy，wjk是关键字的参数
