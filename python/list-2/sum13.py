# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6

def sum13(nums):
    total = 0
    subtract = 0

    for i in range(len(nums)):
        if nums[i] == 13:
            if i < len(nums)-1:
                subtract += nums[i+1]
        else:
            total += nums[i]

    if total >= subtract:
        return total - subtract
    else:
        return total


def sum13(nums):
    total = 0

    if len(nums) == 0:
        return total
    elif nums[0] != 13:
        total += nums[0]

    for i in range(1, len(nums)):
        if nums[i] != 13 and nums[i-1] != 13:
            total += nums[i]

    return total


def sum13(nums):
    total = 0
    i = 0

    while i < len(nums):
        if nums[i] == 13:
            i += 1
        else:
            total += nums[i]
        i += 1

    return total
