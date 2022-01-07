# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

# string_match('xxcaazz', 'xxbaaz') → 3
# string_match('abc', 'abc') → 2
# string_match('abc', 'axc') → 0

def string_match(a, b):
    shorter_str = a if len(a) <= len(b) else b
    match_count = 0
    for i in range(len(shorter_str)-1):
        if a[i:i+2] == b[i:i+2]:
            match_count += 1

    return match_count
