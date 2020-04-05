def test_func(nums):
    nums[2] = nums[2] * 100
    return nums
nums = [1, 2, 3, 4, 5]
test_func(nums)
print nums