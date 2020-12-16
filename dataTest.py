a, b = 33, 77
print("%d" % (a + b))
print("%d" % (b - a))
print("%d" % (a / b))
print("%d" % (b // a))
print("%d, %d" % (a**2, b**3))
print("%d")
c, d, e = hex(a), oct(a), bin(a)
print(c,d, e)
print(str(1))
print(str('abc'))
print(str(None))
print(str(False))
print(bool(1))
print(bool('abc'))
print(bool(None))
print(bool(''))
print(int(1))
# print(int(None))
print(int(False))
print(int(1.2))
print(float(1))
# print(float('abc'))
# print(float(''))
if( a is None):
    print("is None")
else:
    print("is number")

for i in reversed(range(7, 4)):
    print(i, end=' ')

aaaaa = 10
aaa_a = abs(aaaaa)
print(aaa_a)

a_3 = 5
b_3 = a_3 % 3
print(b_3)
print("--------------")
s1 =  {1,2,4,7}
s2 = {2,3,4}
s3 = s1 - s2
print(s3)

fruits = ["banana", "apple", "pear", "watermelon"]
print(sorted(fruits, key = len)[2])

tstr = '12345678'
print(tstr[1:-1:2])

print(tstr[-5:-3])

print('x = {0}'.format(fruits))

xx = [90, 87, 93]
yy = ("Aele", "Bob", "lala")
zz = {}
for i in range(len(xx)):
    zz[i] = [xx[i], yy[i]]
print(zz)

L1 = [1,2,3,4]
print(L1)

def func(x = [], y = [6,7]):
    x.append(8)
    y.append(8)
    return (x+y)
a, b = [1, 2], [3, 4]
t = func(x = a)
t = func(y = b)
print(func(), end = ";")

a = [1,2,3,4]
b = sorted(a, reverse = False)
print(b)

s = '1234567890'
print(s[1:-3])

s = 0
for i in range(1, 11):
    s += i
print(s)

a = "你好"
b = "好"
print((b))

ss = set("123456")
ss2 = set("htslbht")
sorted(ss2)
for i in ss2:
    print(i, end = "")