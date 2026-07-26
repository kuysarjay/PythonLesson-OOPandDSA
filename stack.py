# A stack is a structure developed to store data in a very specific way.
# The alternative name for a stack (but only in IT terminology) is LIFO.
# It's an abbreviation for a very clear description of the stack's behavior:
    # Last In – First Out.
# A stack is an object with two elementary operations,
    # conventionally named push (when a new element is put on the top) and
    # pop (when an existing element is taken away from the top).
    
# Example of Stack:
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())
    

