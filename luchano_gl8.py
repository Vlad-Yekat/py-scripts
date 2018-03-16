
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

t1 = (1,2,[30,40])
t1[-1].append(99)
print(t1)
l1 = [1,2,3,[1,2]]
l2 = list(l1)
print(l2,l1)
l1 = [3,[77,55,44],(7,8,9)]
l2 = list(l1)
l1.append(100)
l1[1].remove(55)
print(l1)
print(l2)
l2[1] += [33,22]
l2[2] += (10,11)
print(l1)
print(l2)
