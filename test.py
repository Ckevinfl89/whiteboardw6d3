import unittest
from whiteboard import solution


class TestThreeSum(unittest.TestCase):
    def test_example1(self):
        self.assertAlmostEqual(solution([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
    def test_example2(self):
        self.assertAlmostEqual(solution([0,1,1]), [])
    def test_example3(self):
        self.assertAlmostEqual(solution([0,0,0]), [[0,0,0]])
    def test_all_negative_numbers(self):
        self.assertAlmostEqual(solution([-5,-4,-3,-2,-1]), [])
    def test_all_positive_numbers(self):
        self.assertAlmostEqual(solution([1,2,3,4,5]), [])
    def test_one_positive_number(self):
        self.assertAlmostEqual(solution([-1,-1,2,3,4]),[[-1,-1,2]])
    def test_one_negative_number(self):
        self.assertAlmostEqual(solution([-2,-1,0,1,2]), [[-2,0,2],[-1,0,1]])
    def test_no_duplicates(self):
        self.assertAlmostEqual(solution([-1, 0, 1, 0]), [[-1, 0, 1]])

if __name__ == '__main__':
    unittest.main()