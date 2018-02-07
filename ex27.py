a = True and True #True
print(a)
b = False and True #False
print(b)
c = 1 == 1 and 2==1 #False
print(c)
d = "Test" == "Test" #True
print(d)
e = 1 == 1 or 2 != 1 #True
print(e)
f = True and 1 == 1 #True
print(f)
g = False and 0 != 0 #False
print(g)
h = True or 1 == 1 #True
print(h)
i = "Test" == "Testing" #False
print(i)
k = 1 != 0 and 2 == 1 #False
print(k)
l = "Test" != "Testing" #True
print(l)
m = "Test" == 1 #False
print(m)
n = not (True and False) #True
print(n)
o = not (1 == 1 and 0 != 1) #False
print(o)
p = not (10 == 1 or 1000 == 1000) #False
print(p)
q = not (1 != 10 or 3 == 4) #False
print(q)
r = not ("Testing" == "Testing" and "Zed" == "Cool Guy") #True
print(r)
s = 1 == 1 and (not("Testing" == 1 or 1 == 0)) #True
print(s)
t = "chunky" == "bacon" and (not(3 == 4 or 3 == 3)) #False
print(t)
u = 3 == 3 and (not("Testing" == "Testing" or "Python" == "Fun")) #False
print(t)