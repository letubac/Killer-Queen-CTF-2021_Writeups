f=''
a = "rwhxi}eomr\\^`Yf]XdThbQd^TYL&\x13g"
for i in range(len(a)):
    c = ord(a[i])
    c = c - 7
    c = c + i
    f += chr(c)
print(f)