#calculator.py

class Calculator:
    """Simple calculator class.

    This class provides basic arithmetic operations:
    addition, subtraction, multiplication, and division.
    """

    def add(self, a, b):
        """Return the sum of a and b.

        Args:
            a (int or float): First number
            b (int or float): Second number

        Returns:
            int or float: Sum of a and b
        """
        return a + b

    def divide(self, a, b):
        """Return the division of a by b.

        Raises:
            ValueError: If b is zero

        Args:
            a (int or float): Numerator
            b (int or float): Denominator

        Returns:
            float: Result of division
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
