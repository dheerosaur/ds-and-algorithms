"""
Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

"""
from typing import List


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = 0
        return maxSum


def test():
    "Testing the solution"
    sol = Solution()
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


if __name__ == '__main__':
    test()
