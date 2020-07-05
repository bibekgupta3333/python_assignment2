# 2. Write an if statement to determine whether a variable holding a year
# is a leap year.
import unittest


def isLeapYear(year):
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    return False


class TestArea(unittest.TestCase):
    def runTest(self):
        self.assertTrue(
            isLeapYear(2000))


if __name__ == "__main__":
    input_year = int(input("please enter a year to check leap year or not: "))
    print(f'{input_year} is leap year',
          isLeapYear(input_year))
    unittest.main()
