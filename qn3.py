# 3. Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text.

import unittest


def getAnagramFromParagraph(input_string):
    word_list = input_string.split()
    anagram_list = []
    for word in word_list:
        for each in word_list:
            if sorted(word) == sorted(each) and word != each:
                anagram_list.append(word)
    return sorted(set(anagram_list))


class TestArea(unittest.TestCase):
    def runTest(self):
        self.assertEqual(getAnagramFromParagraph("bang bagn ram mar sam  take bigtake ma am bigta ma mas asm"), [
                         'am', 'asm', 'bagn', 'bang', 'ma', 'mar', 'mas', 'ram', 'sam'])


if __name__ == "__main__":
    input_year = "bang bagn ram mar sam  take bigtake ma am bigta ma mas asm"
    print(getAnagramFromParagraph(input_year))
    unittest.main()
