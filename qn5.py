# 5. Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.
import unittest


def createSortedPeopleList():
    people = [('ram', 'basnet', 21), ('sikxant', 'lama', 23), ('antman', 'brandster', 32),
              ('John', 'smith', 12), ('bhanu', 'bhakta', 200), ('abhram', 'linconn', 150)]
    people.sort(key=lambda e: e[2])
    return people


class TestArea(unittest.TestCase):
    def runTest(self):
        self.assertEqual(createSortedPeopleList(), [('John', 'smith', 12), ('ram', 'basnet', 21), (
            'sikxant', 'lama', 23), ('antman', 'brandster', 32), ('abhram', 'linconn', 150), ('bhanu', 'bhakta', 200)])


if __name__ == "__main__":

    print(createSortedPeopleList())
    unittest.main()
