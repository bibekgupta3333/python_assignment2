# 19. Write a Python class to find validity of a string of parentheses, '(',
# ')', '{', '}', '[' and ']. These brackets must be close in the correct order,
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid


import unittest


def isParenthesesValid(input_string):
    left = []
    right = []
    left_parentheses = list('([{')
    right_parentheses = list(')]}')
    for each in input_string:
        if each in left_parentheses:
            left.append(each)
        if each in right_parentheses:
            right.append(each)
    return ['valid' if len(left) == len(right) else 'invalid'][0]


class TestArea(unittest.TestCase):
    def runTest(self):
        self.assertEqual(isParenthesesValid('{}()[]'), 'valid')


if __name__ == "__main__":
    print(isParenthesesValid("{}[[{}]]"))
    unittest.main()
