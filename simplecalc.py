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
