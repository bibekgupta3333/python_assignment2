# 12. Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.
import unittest
import string


def is_palindrome(strings):
    characterArr = list(strings.split()[0].lower())
    letterArr = []
    for char in characterArr:
        if char in string.ascii_lowercase:
            letterArr.append(char)
    letterArr.reverse()
    return ('').join(letterArr)


class TestArea(unittest.TestCase):
    def runTest(self):
        self.assertEqual(is_palindrome("bibek"), "kebib")


if __name__ == "__main__":
    print(is_palindrome('bibeka'))
    unittest.main()
