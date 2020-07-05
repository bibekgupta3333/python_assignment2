# 10. Write a function that takes camel-cased strings (i.e.
# ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument,
# separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.
import unittest


def getSnakeCaseOfCamelCase(input_string, separator="_"):
    list_char = list(input_string)
    for each in input_string:
        if each.isupper():
            index = list_char.index(str(each))
            list_char[index] = "_"+each.lower()
    list_char = ('').join(list_char)[1:]
    return list_char.replace("_", separator)


class TestArea(unittest.TestCase):
    def runTest(self):
        self.assertEqual(getSnakeCaseOfCamelCase(
            'ThisIsCamelCased', "-"), 'this-is-camel-cased')


if __name__ == "__main__":
    input_string = 'ThisIsCamelCasedWhatIsTheName'
    print(getSnakeCaseOfCamelCase(input_string))
    print('using seprator:', getSnakeCaseOfCamelCase(input_string, "-"))
    unittest.main()
