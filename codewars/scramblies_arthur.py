from collections import Counter


def scramble(str1, str2):
    counter1 = Counter(str1)
    counter2 = Counter(str2)
    for char, count in counter2.items():
        if counter1.get(char, 0) < count:
            return False
    return True
