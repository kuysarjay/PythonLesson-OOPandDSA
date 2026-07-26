# The lambda function is a concept borrowed from mathematics, more specifically,
    # from a part called the Lambda calculus, but these two phenomena are not the same.
# A lambda function is a tool for creating anonymous functions.

# The map(fun, list) function creates a copy of a list argument,
    # and applies the fun function to all of its elements,
    # returning a generator that provides the new list content element by element.
    
# Example:
short_list = ['mython', 'python', 'fell', 'on', 'the', 'floor']
new_list = list(map(lambda s: s.title(), short_list))
print(new_list)

# The filter(fun, list) function creates a copy of those list elements,
    # which cause the fun function to return True.
    # The function's result is a generator providing the new list content element by element.

# Example:
short_list = [1, "Python", -1, "Monty"]
new_list = list(filter(lambda s: isinstance(s, str), short_list))
print(new_list)

