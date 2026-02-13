#Find MAX number (Without Inbuilt Func)
nums = [10, 20, 5, 40, 25]

min_num = nums[0]

for i in nums:
    if i < min_num:
        min_num = i

print(min_num)

#Find SECOND MINIMUM
nums = [10, 20, 5, 40, 25]

min1 = min2 = float('inf')

for i in nums:
    if i < min1:
        min2 = min1
        min1 = i
    elif i < min2 and i != min1:
        min2 = i

print(min2)

#Find MIN & MAX in ONE LOOP (Popular)
nums = [10, 20, 5, 40, 25]

min_num = max_num = nums[0]

for i in nums:
    if i < min_num:
        min_num = i
    elif i > max_num:
        max_num = i

print(min_num, max_num)

#Count EVEN & ODD numbers
nums = [10, 21, 30, 45, 50]

even = odd = 0

for i in nums:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even, "Odd:", odd)

#Reverse a list (without slicing)
nums = [1, 2, 3, 4]

rev = []
for i in nums:
    rev = [i] + rev

print(rev)

#Check if number is PRIME
n = 7
is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

print(is_prime)

#Find SUM of list
nums = [10, 20, 30]

total = 0
for i in nums:
    total += i

print(total)

#Find DUPLICATES in list
nums = [1, 2, 3, 2, 4, 1]

seen = set()
dup = set()

for i in nums:
    if i in seen:
        dup.add(i)
    else:
        seen.add(i)

print(list(dup))

#Add Element at End
a=[2,3,4]
a.append(6)
print(a)

#Add Element at specific index
l=[1,5]
l.insert(1,2)
print(l)

#Add Multiple Elements
h=[1,2]
h.extend([3,4,5])
print(h)

#Remove the spcefic element
a=[1,6,3]
a.remove(6)
print(a)

#Remove element by index (default last)
a=[1,2,3]
a.pop()
print(a)

#Remove all element
a=[1,4,7]
a.clear()
print(a)

#Sorting the list
a=[1,5,9]
a.sort()
print(a)

#Find index of element
l=[10,20,30]
print(l.index(20))

#Count Occurrences
a=[1,2,2,3]
print(a.count(2))

#Reverse List
a=[1,2,3,4]
a.reverse()
print(a)

#Copy List
a=[1,2]
b=a.copy()
print(b)

#Length of list
a=[1,2,3,5,6]
print(len(a))

#Return the max&min value from a list
a=[1,5,3]
print(min(a))

#Return the total of all element in a list
a=[1,2,3]
print(sum(a))




