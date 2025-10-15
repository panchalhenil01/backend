t=(1,2,10,20,1.1,2.2,"tops",[100,200,300],True,"python",100,200,"java")

print(t)
print(t.count(1))
print(t.index(10))
print(t[7])
t[7].append(400)
print(t)

for i in t:
    print(i)
print(300 in t)
print(t[7][2])

    

