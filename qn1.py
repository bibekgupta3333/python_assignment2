# 1. Create a variable, paragraph, that has the following content:
# "Python is a great language!", said Fred. "I don't ever remember
# having this much fun before."
import unittest


def assginContentIntoParagraphVar():
    paragraph = '"Python is a great language!", said Fred. "I don\'t ever remember having this much fun before."'
    return paragraph


class TestArea(unittest.TestCase):
    def test_paragraph(self):
        self.assertEqual(
            assginContentIntoParagraphVar(), '"Python is a great language!", said Fred. "I don\'t ever remember having this much fun before."')


if __name__ == "__main__":
    print(assginContentIntoParagraphVar())
    unittest.main()
