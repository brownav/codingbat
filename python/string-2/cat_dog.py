# Return True if the string "cat" and "dog" appear the same number of times in the given string.

# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(str):
    cat_count = 0
    dog_count = 0
    for x in range(len(str)-2):
        if str[x:x+3] == 'cat':
            cat_count += 1
        if str[x:x+3] == 'dog':
            dog_count += 1

    return cat_count == dog_count
