import sys
import math
import random

permutations_list = []


# Fisher-Yates implementation to randomly shuffle and generate a permutation
def generate_permutation(a, n):
    list_range = range(0, n)
    for i in list_range:
        j = random.randint(list_range[0], list_range[-1])
        a[i], a[j] = a[j], a[i]
    # Add the non-separated sequence of character to a list
    permutations_list.append(''.join(a))


if len(sys.argv) != 2:
    sys.stderr.write('Exactly one argument is required\n')
    sys.exit(1)

word = sys.argv[1]

# call 20 times to get 20 random permutations of the characters in a given word
for i in range(20):
    generate_permutation(list(word), len(word) - 1)

print(permutations_list)

