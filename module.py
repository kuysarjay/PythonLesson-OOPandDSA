# Module is a File containing definition and statements.
# Module is defined by its name. If you want to use any module you need to know the name.
# To use the Module you need to call it by 'import' followed by the module name. (eg,. import math)

# Example how to use a Module:
import math as m # Aliasing


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14

print(sin(pi/2))
print(m.sin(m.pi/2))
