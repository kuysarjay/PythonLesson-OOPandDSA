# String methods are built-in functions used to perform operations on strings,
    # such as changing case, searching, replacing, splitting, and checking string content.
    
# 1. Some of the methods offered by strings are:
    # capitalize() – changes all string letters to capitals;
    # center() – centers the string inside the field of a known length;
    # count() – counts the occurrences of a given character;
    # join() – joins all items of a tuple/list into one string;
    # lower() – converts all the string's letters into lower-case letters;
    # lstrip() – removes the white characters from the beginning of the string;
    # replace() – replaces a given substring with another;
    # rfind() – finds a substring starting from the end of the string;
    # rstrip() – removes the trailing white spaces from the end of the string;
    # split() – splits the string into a substring using a given delimiter;
    # strip() – removes the leading and trailing white spaces;
    # swapcase() – swaps the letters' cases (lower to upper and vice versa)
    #title() – makes the first letter in each word upper-case;
    # upper() – converts all the string's letter into upper-case letters.

#2. String content can be determined using the following methods (all of them return Boolean values):
    # endswith() – does the string end with a given substring?
    # isalnum() – does the string consist only of letters and digits?
    # isalpha() – does the string consist only of letters?
    # islower() – does the string consists only of lower-case letters?
    # isspace() – does the string consists only of white spaces?
    # isupper() – does the string consists only of upper-case letters?
    # startswith() – does the string begin with a given substring?

# Example of String Methods:
text = "  hello world  "
mixed = "PyThOn"
letters = "Python"
alnum = "Python123"
spaces = "   "
fruits = ["apple", "banana", "orange"]

print("capitalize():", text.capitalize())
print("center():", text.strip().center(20, "-"))
print("count():", text.count("l"))
print("join():", ", ".join(fruits))
print("lower():", mixed.lower())
print("lstrip():", text.lstrip())
print("replace():", text.replace("world", "Python"))
print("rfind():", text.rfind("l"))
print("rstrip():", text.rstrip())
print("split():", text.strip().split())
print("strip():", text.strip())
print("swapcase():", mixed.swapcase())
print("title():", text.title())
print("upper():", text.upper())

print("endswith():", text.strip().endswith("world"))
print("isalnum():", alnum.isalnum())
print("isalpha():", letters.isalpha())
print("islower():", "python".islower())
print("isspace():", spaces.isspace())
print("isupper():", "PYTHON".isupper())
print("startswith():", text.strip().startswith("hello"))