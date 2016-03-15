print  (ord('v'))
print (chr(55))
print(b'A'.decode('ascii'))
print('a'.encode('ascii'))
print ('和好'.encode('utf-8'))#纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes
print (len('ed'.encode('ascii')))