
def hello():
    print("Hello, World!")


def prime():
    # add an indented block of code here
    pass


def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0:
        return -1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

import unittest
class TestFactorialFunction(unittest.TestCase):
    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120, "Should be 120")

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1, "Should be 1")

    def test_factorial_negative(self):
        self.assertEqual(factorial(-1), "Factorial does not exist for negative numbers", "Should return a specific message")

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1, "Should be 1")

if __name__ == '__main__':
    unittest.main()