#Reverse a String
#Using slicing
s = "python"
print(s[::-1])

#Using Loop
s = "python"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)

#Check Palindrome String
s = "madam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#Count Vowels and Consonants
s = "Hello World"
vowels = "aeiou"
v = c = 0

for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1

print("Vowels:",v)
print("Consonants:",c)

#Count Frequency of Characters
s = "Aakash"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)

#Remove Duplicates from String
s = "Karan"
result = ""

for ch in s:
    if ch not in result:
        result += ch

print(result)

#Find First Non-Repeating Character
s = "aabbcde"

for ch in s:
    if s.count(ch) == 1:
        print("First non-repeating:",ch)
        break

#Check Anagram
s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")

#Count Words in a String
s = "Python is very easy"
words = s.split()
print("Word count:",len(words))

#Find Duplicate Characters
s = "Programming"
duplicates = set()

for ch in s:
    if s.count(ch) > 1:
        duplicates.add(ch)

print(duplicates)

#Replace Space with Hyphen
s = "Hello world python"
print(s.replace(" ", "-"))





