class Calculator:
    def add(self, a, *b):
        return a +(sum(b))

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, *b):
        result = a
        for x in b:
            result *= x
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
c1=Calculator()
print(c1.add(2,3,4,6,0,7,))
print(c1.subtract(10, 5))
print(c1.multiply(2,3,5,6,7,8,9))
print(c1.divide(100,9))