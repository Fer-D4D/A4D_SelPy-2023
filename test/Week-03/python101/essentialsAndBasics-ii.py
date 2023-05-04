# Conditional Statements

# We all know what's wrong with conditionals, right? Basically it's the same as in real life or any other language.
# Here we have the famous "if" which does nothing but validate whether a statement is true or not.
# Let's try something, excuse the obviousness
if 5 < 10:
    print("Evidently this statement is true")

# Or something even more obvious
if True:
    print("This other one is also obvious")

# but what happens if the condition is not fulfilled, and we want to do something when it is, well here is Mr. "else".

if False:
    print("We force that this is never used")
else:
    print('Mr. "else" doing his thing')

# Now that we have seen how it works and since we are already experts in the use of variables,
# it's time to give it our all

condition_a = 5
condition_b = 10

if not condition_a > condition_b or condition_b == 11:
    print("It is almost obvious that this is a true statement.")
else:
    print("It is almost obvious that this is a false statement.")



