# function for determining which Collatz rule to apply
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


# function that stores the full Collatz Sequence of each number
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

# CHANGE THIS n to set the highest number you would like to check for Collatz Sequence length
for i in range(1, n + 1):
    sequence_check = []
    sequence_check += get_sequence(i)

    if len(sequence_check) > len(new_sequence):
        new_sequence = sequence_check

# prints the starting number of the sequence; you can delete the [0] to print the whole Collatz Sequence if you would like
print(new_sequence[0])
