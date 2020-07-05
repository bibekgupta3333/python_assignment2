# 11. Create a variable, filename. Assuming that it has a three-letter
# extension, and using slice operations, find the extension. For
# README.txt, the extension should be txt. Write code using slice
# operations that will give the name without the extension. Does your
# code work on filenames of arbitrary length?
import unittest


def getExtension(*filenames):
    filenames = list(filenames)
    extension = []
    if type(filenames) is list and len(filenames) > 1:
        for each in filenames:
            if len(each.split('.')[-1]) >= 3 and len(each.split('.')) < 3:
                each = each.split(".")[-1]
                extension.append(each)
        print(len(extension))
        if len(extension) < 2:
            return extension[0]
        else:
            return extension
    else:
        return filenames[0].split(".")[-1]


class TestArea(unittest.TestCase):
    def runTest(self):
        self.assertEqual(getExtension("bibek.txt"), "txt")
        self.assertEqual(getExtension('bibek.pdf', 'gupta.money',
                                      'gupta.money', 'gupta.money', 'gupta.money'), ["pdf", "money", "money", "money", "money"])


if __name__ == "__main__":
    filenames = ['bibek.pdf', 'gupta.money',
                 'gupta.money', 'gupta.money', 'gupta.money']
    filename = "bibek.txt"
    print(getExtension(*filenames))
    unittest.main()
