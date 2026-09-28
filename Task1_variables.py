# Task 1: Variables

# Question 1
pi = 22/7
print("Value of pi:", pi)
print("Data type:", type(pi))

# Question 2
print("\nQuestion 2")
try:
    exec("for = 4")
except SyntaxError:
    print("'for' is a reserved keyword in Python, so it cannot be used as a variable name.")

# Question 3
principal = 10000
rate = 5
time = 3

simple_interest = (principal * rate * time) / 100

print("\nSimple Interest for 3 years:", simple_interest)