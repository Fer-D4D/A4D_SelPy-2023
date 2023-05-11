# Empty functions
def empty_function():
    pass


# Passing Arguments to a Function

def add(j, i):
    return j + i


print("Printing result of the Passing Arguments to a Function example: " + str(add(2, 2)))


# Passing Arguments to a Function with default values
def add_def_values(j=2, i=3):
    return j + i


print("Printing result of the Passing Arguments to a Function with default values example: " + str(add_def_values()))

# Now let's imagine we want to print our results every time we made a calculation
a = 5
b = 4

x = a + b
print(f"Result of adding {a} to {b} is: {x}")

x = a - b
print(f"Result of subtracting {a} from {b} is: {x}")


# This is hypothetical and obviously such a function is not really necessary,
# but it will serve to illustrate the point.

def print_results(addend1, sign, addend2):
    control = True
    subtext1 = ""
    subtext2 = ""
    result = 0
    if sign == "+":
        subtext1 = "adding"
        subtext2 = "to"
        result = addend1 + addend2
    elif sign == "-":
        subtext1 = "subtracting"
        subtext2 = "from"
        result = addend1 - addend2
    else:
        print("Unsupported operation")
        control = False
    if control:
        print(f"Result of {subtext1} {addend1} {subtext2} {addend2} is: {result}")


print_results(6, "+", 5)
print_results(6, "-", 5)
print_results(6, "*", 5)
