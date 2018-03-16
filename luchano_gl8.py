
a = [1,2,3]
b = a
a.append(4)
b.append(5)
print(id(a),a)
print(id(b),b)
print(a is b)
print(a == b)
print(a.__eq__(b))

c = 1
d = c
c += 0
print(id(d),d)
print(id(c),c)
print(c.__eq__(d))

e = 'ddd'
f = e
e = e+'r'
print(id(e),e)
print(id(f),f)

