# In Python, we can pass a variable number of arguments to a function using special symbols.
    # There are two special symbols:
        # *args (Non Keyword Arguments)
        # **kwargs (Keyword Arguments)
# We use *args and **kwargs as an argument when we are unsure about
    # the number of arguments to pass in the functions.
    
# Python has *args which allow us to pass the variable number of non keyword arguments to function.
# In the function, we should use an asterisk * before the parameter name to pass variable
    # length arguments. The arguments are passed as a tuple and these passed arguments make
    # tuple inside the function with same name as the parameter excluding asterisk *.
    
def adder(*num):
    sum = 0
    
    for n in num:
        sum = sum + n

    print("Sum:",sum)

adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)

# Python passes variable length non keyword argument to function using *args but we cannot
    # use this to pass keyword argument.
    # For this problem Python has got a solution called **kwargs,
    # it allows us to pass the variable length of keyword arguments to the function.
# In the function, we use the double asterisk ** before the parameter name to denote this type of argument.
# The arguments are passed as a dictionary and these arguments make a dictionary inside
    # function with name same as the parameter excluding double asterisk **.
    
def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com",
      Country="Wakanda", Age=25, Phone=9876543210)

# *args and **kwargs are special keyword which allows function to take variable length argument.
# *args passes variable number of non-keyworded arguments and on which
    # operation of the tuple can be performed.
# **kwargs passes variable number of keyword arguments dictionary to function on which
    # operation of a dictionary can be performed.
# *args and **kwargs make the function flexible.