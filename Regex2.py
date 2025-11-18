import re

pattern = r"\d+"
string = "I have 12 apples, 15 bananas, and 100 grapes"
result = re.findall(pattern, string)

print(result)
