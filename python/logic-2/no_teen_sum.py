# Given 3 int values, a b c, return their sum. However, if any of the values is a teen - - in the range 13..19 inclusive - - then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times(i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().

# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
    sum = 0
    for num in [a, b, c]:
        if 12 < num < 20:
            sum += fix_teen(num)
        else:
            sum += num
    return sum


def fix_teen(num):
    if num == 15 or num == 16:
        return num
    else:
        return 0

# ------------------------------ #


def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


def fix_teen(num):
    if 12 < num < 20 and num != 15 and num != 16:
        return 0

    return num
