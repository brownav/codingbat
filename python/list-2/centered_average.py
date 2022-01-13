# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.

# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

def centered_average(nums):
    total = nums[0]
    min_num = nums[0]
    max_num = nums[0]

    for i in range(1, len(nums)):
        total += nums[i]
        if min_num < nums[i]:
            min_num = nums[i]
        if max_num > nums[i]:
            max_num = nums[i]

    return (total - max_num - min_num) / (len(nums) - 2)


def centered_average(nums):
    return (sum(nums) - max(nums) - min(nums)) / (len(nums) - 2)
