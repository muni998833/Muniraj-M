#  Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.  
#  Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’   Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Cannot divide by zero"

# Example usage:
calc = Calculator(0,5)
print("Addition:", calc.add())
print("Subtraction:", calc.subtract())
print("Multiplication:", calc.multiply())
print("Division:", calc.divide())