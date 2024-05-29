def p1(source, target):
    char_set = set(source)
    for char in target:
        if char not in char_set:
            return -1

    source_pointer = 0
    count = 0

    for char in target:
        if source_pointer == 0:
            count += 1

        while source[source_pointer] != char:

            source_pointer = (source_pointer + 1) % len(source)
            if source_pointer == 0:
                count += 1

        source_pointer = (source_pointer + 1) % len(source)

    return count


print(p1("abc","abcbc"))
print(p1("abc", "acdbc"))
print(p1("xyz","xzyxz"))



