
def max_sum_array(nums):
    if len(nums) < 3:
        return max(nums) if nums else 0

    mx1, mx2 = nums[0], nums[1]
    for num in nums[2:]:
        mx1, mx2 = max(mx1, mx2), max(num, mx1 + num)
    return max(mx1, mx2)


if __name__ == '__main__':
    cases = [
        [-2, 1, 3, -4, 5],
        [3, 7, 4, 6, 5],
        [2, 1, 5, 8, 4],
        [3, 5, -7, 8, 10],
    ]
    for case in cases:
        print(max_sum_array(case))
