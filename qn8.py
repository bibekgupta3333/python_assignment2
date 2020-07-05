# 8. Write a function, is_prime, that takes an integer and returns True if
# the number is prime and False if the number is not prime.
import unittest


def is_prime(input_int):
    counter = 0
    for i in range(1, input_int+1):
        if input_int % i == 0:
            counter += 1
    if counter == 2:
        return True
    return False


class TestArea(unittest.TestCase):
    def runTest(self):
        self.assertTrue(is_prime(5))


if __name__ == "__main__":
    input_int = int(input('Please enter a integer to check prime: '))
    print(is_prime(input_int))
    unittest.main()
