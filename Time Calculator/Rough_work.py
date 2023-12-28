h = ["Boy","Dog"]
a = ','.join(h)
print(a)
print(type(h))
a = ['2','+ 6']
b = [' 2','+ 3']
c = ['4','9']
print(list(zip(a,b,c)))
A  = '11:30 AM'
a = A.split(':')
print(a)
z = a[1].split(' ')
z.insert(0,a[0])
print(z)


