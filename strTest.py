a, b = "hello", "abc"

c = a + b
print("%s" % (c,))
print("%s" % (c*3))
print("%d" % len(c))
print("%s" % 'h' in a)
print("%s" % a[2])
print("%d" % (ord(a[0])))
print("%s" % (chr(ord(a[0]))))
x, y, z = "你好", "早上好", "abcdefg12345"
print("%s" % (x, ))
print("%d" % (len(x), ))
j = z[3:9]
k = z[:6:-1]
l = z[5::]
m = z[:9:2]
print("%s" % (j, ))
print("%s" % (k, ))
print("%s" % (l, ))
print("%s" % (m, ))
t = "Mike and Tom"
r = t.split(' ')
print("%s" % (r,))
r[0].upper()
print("%s, %s, %s" % (r[0].upper(), r[1].lower(), r[2].swapcase()))

# e = t.ljust(30)
# e = t.center(30)
e = t.rjust(30)
w = t.replace("Mike", "Jerry")
print("%s" % (e, ))
print("%s" % (w, ))