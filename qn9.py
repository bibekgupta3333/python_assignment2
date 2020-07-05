# 9. Write a binary search function. It should take a sorted sequence and
# the item it is looking for. It should return the index of the item if found.
# It should return -1 if the item is not found.
import unittest


def binarySearch(arr, key):
    arr_list = arr.copy()
    arr_list.sort()
    print('sorted list', arr_list)

    def bs(arr, key):
        arr.sort()
        mid = len(arr)//2
        midElm = arr[mid]
        if arr[mid] == key:
            return arr[mid]
        elif key > midElm and len(arr) > 1:
            arr = arr[mid:]
            return bs(arr, key)
        elif key < midElm and len(arr) > 1:
            arr = arr[:mid]
            return bs(arr, key)
        else:
            return -1
    return [arr_list.index(bs(arr, key)) if bs(arr, key) != -1 else -1][0]


class TestArea(unittest.TestCase):
    def runTest(self):
        self.assertEqual(binarySearch(
            [1, 30, 40, 50, 60, 70, 100, 105], 109), -1)


if __name__ == "__main__":
    input_list = [1, 30, 40, 50, 60, 70, 100, 105]
    print(binarySearch(input_list, 20))
    unittest.main()
