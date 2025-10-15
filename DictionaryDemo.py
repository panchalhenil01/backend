d={110:"Harshil",343:"Henil",989:"Priyanshu",767:"Akash",656:"Yash",900:"Ansh",767:"Karan",322:"Aniket"}
print(d)
print(d[343])
print(d.get(767))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(656))
print(d)
print(d.popitem())
print(d)
d1={111:"Jenil",222:"Rohan",333:"Guddu",444:"Suraj",555:"Harshad"}
d.update(d1)
print(d)

for i in d:
    print(i," : ",d[i])
    
    
    


