# What could be more basic than understanding how the language handles data?
# Well Python makes it easy, let's see some examples:
def name_str(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]


def analizame(variable):
    print("La variable '" + name_str(variable, globals())[0] + "' contiene el valor: ["
          + str(variable) + "] y es del tipo " + str(type(variable)) + "")


# It couldn't be any different, let's start by defining a variable and assigning it a text string
#
mi_variable = "Hola Mundo"
# Don't pay too much attention to the following line, it is a function defined to obtain information from a variable,
# yes functions! we will see them soon
analizame(mi_variable)
# Pay attention to the following the variable we used to store a text, now we will use it to store an enter number,
# how practical is python, isn't it?
mi_variable = 12
# We use the same function to analyze our variable (a function we haven't seen yet,
# but I promise we will soon).
analizame(mi_variable)
# We will do it again, same variable that has stored a text, then an integer,
# now we will assign a logical or boolean value, why? because Python is that cool.
mi_variable = False
# Analyzing our variable
#
analizame(mi_variable)
# Now we create a new variable with the current content of our first variable
#
copia_de_mi_variable = mi_variable
# And we do it again now we assign a decimal numerical value to our first variable
#
mi_variable = 1.34
# Analyzing our variables
#
analizame(copia_de_mi_variable)
analizame(mi_variable)
# Now that we get the point, Python is a cool language! Let's see a data type that we will find
# very useful, yes, the lists
una_lista = [1, 2, 3, 'a', 'b', 'c']
# Analyzing our list
#
analizame(una_lista)
# And to validate the point, how about a list built with the values stored by another list and one of our beloved
# variables?
otra_lista = [una_lista, mi_variable]
# Analyzing our list, it is a beauty, isn't it?
#
analizame(otra_lista)
# Now let's look at something even more useful, dictionaries.
#
un_dictionario = {"uno":"eins", "dos":"zwei"}
analizame(un_dictionario)


