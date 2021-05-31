# CONTROL FLOW

x= range(10)
print(x)


a=range(1,10)
for x in a:
    print(x)

b=range (100,200)
for a in b:
    if a%2==0:
        print(a)

c=range (1000)
for s in c:
    if s%2!=0:
        print(s)
n=range(1000)
for y in n:
    if y%2==0:
        print("{} is divisible by two".format(y))
    else:
        print("{} it is not divisible by two".format(y))
w=range(100)
for d in w:
    if d%2==0:
        print("{} is divisible by two".format(d))
    elif d%3==0:
        print("{} is divisible by three".format(d))
    else:
        print("{} is not divisible by either 2 or 3".format(d))

k=range(100)
for u in k:
    if u%5==0:
        print("{} is divisible by five".format(u))
    elif u%7==0:
        print("{} is divisible by seven".format(u))
    else:
        print("{} is not divisible by both 5 and 7".format(u))

x=1
while x<10:
    print(x)
    x +=1

y=100
while y >= 30:
    print(y)
    y -=30

x=100
while x >=30:
    print(x)
    if x < 50:
        break
    x -= 10

x=1
while x < 10:
    x += 1
    if x%3 == 0:
        continue
    print(x)

z=1
while z <50:
    z +=1
    if z%5 == 0:
        continue
    print(z)    






