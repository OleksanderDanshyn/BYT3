from abc import ABC, abstractmethod

class ICalculator(ABC):

    @abstractmethod
    def addition(self):
        pass

    @abstractmethod
    def subtraction(self):
        pass

    @abstractmethod
    def multiplication(self):
        pass

    @abstractmethod
    def division(self):
        pass



class Calculator(ICalculator):
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

        if operation not in ['+', '-', '*', '/']:
            raise ValueError(f"Invalid operation: {operation}. Must be +, -, *, or /")


    def addition(self):
        return self.a + self.b


    def subtraction(self):
        return self.a - self.b


    def multiplication(self):
        return self.a * self.b


    def division(self):
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.a / self.b


    def calculate(self):
        if self.operation == '+':
            return self.addition()
        elif self.operation == '-':
            return self.subtraction()
        elif self.operation == '*':
            return self.multiplication()
        elif self.operation == '/':
            return self.division()
        else:
            raise ValueError(f"Unsupported operation: {self.operation}")


    def __str__(self):
        try:
            result = self.calculate()
            return f"{self.a} {self.operation} {self.b} = {result}"
        except ZeroDivisionError as e:
            return f"{self.a} {self.operation} {self.b} = Error: {e}"

if __name__ == "__main__":
    print("=== Calculator Demonstration ===\n")

    calc1 = Calculator(10, 5, '+')
    print(f"Addition: {calc1}")

    calc2 = Calculator(10, 5, '-')
    print(f"Subtraction: {calc2}")

    calc3 = Calculator(10, 5, '*')
    print(f"Multiplication: {calc3}")

    calc4 = Calculator(10, 5, '/')
    print(f"Division: {calc4}")
