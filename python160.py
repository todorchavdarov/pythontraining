import math


def sigmoid(x):                         # Define logistic function used for the second task
    return 1 / (1 + math.exp(-x))


names = ['Carina', 'Ivan', 'Sophia', 'Jenn', 'Phil']

"""Lambda to get first element from the list"""
getFirstElement = lambda element: element[0]

print(getFirstElement(names))


"""Map a lambda which applies the logistic function to the list [-3, -5, 1, 4]
Round each number to 4 decimal places."""

list_numbers = [-3, -5, 1, 4]

list(map(lambda n: n * -1, list_numbers))
print(list(map(lambda x: round(x, 4), list(map(lambda number: sigmoid(number), list_numbers)))))
