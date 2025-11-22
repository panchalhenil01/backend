class MathOperations:
    def multiply(self, a, b, c=1):
        return a * b * c

math = MathOperations()
print(math.multiply(5, 10))       
print(math.multiply(5, 10, 15))  
