# 20. Write a Python class to find the three elements that sum to zero
# from a list of n real numbers.
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# Output : [[-10, 2, 8], [-7, -3, 10]]
import unittest


def getThreeElementSumToZero(input_list):
    output_list = []
    if type(input_list) is list:
        for i in input_list:
            for j in input_list:
                for k in input_list:
                    if(i+j+k == 0):
                        if sorted([i, j, k]) in output_list:
                            continue
                        output_list.append(sorted([i, j, k]))
        return output_list
    else:
        return print('please pass argument as a list')


class TestArea(unittest.TestCase):
    def runTest(self):
        self.assertEqual(getThreeElementSumToZero(
            [-25, -10, -7, -3, 2, 4, 8, 10]), [[-10, 2, 8], [-7, -3, 10]])


if __name__ == "__main__":
    print(getThreeElementSumToZero([-25, -10, -7, -3, 2, 4, 8, 10]))
    unittest.main()
