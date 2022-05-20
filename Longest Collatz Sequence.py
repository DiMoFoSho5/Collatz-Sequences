def even_check(x):
    if x % 2 == 0:
        return True
    else:
        return False


# function that applies the Collatz rules
def do_math(x):
    if even_check(x) is True:
        number = x / 2
    else:
        number = (3 * x) + 1

    return number


def get_sequence(x):
    sequence = []
    next_num = 0
    sequence += [x]
    next_num += do_math(x)

    while next_num != 1:
        sequence += [next_num]
        next_num = do_math(next_num)

        if next_num == 1:
            sequence += [1]
            break

    return sequence


new_sequence = []

for i in range(1, 1000000):
    sequence_check = []
    sequence_check += get_sequence(i)

    if len(sequence_check) > len(new_sequence):
        new_sequence = sequence_check

print(new_sequence[0])
