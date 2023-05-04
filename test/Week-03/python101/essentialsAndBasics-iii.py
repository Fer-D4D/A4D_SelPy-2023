# What could be more basic than understanding how the language handles data?
# Well Python makes it easy, let's see some examples:
una_lista = [1, 2, 3, 'a', 'b', 'c']

print(range(2, 6))
print("--------------------")

for idx in range(6):
    print(una_lista[idx], end=" ")
print()
print("--------------------")

for idx in una_lista:
    print(idx, end=" ")
print()
print("--------------------")

for idx in range(16):  # for(int idx=0; idx < 16; idx++)
    print(idx, end=" ")
print()
print("--------------------")

for idx in range(1, 10): # for(int idx=1; idx < 16; idx++)
    print(idx, end=" ")
print()
print("--------------------")

for idx in range(0, 10, 2):
    print(idx, end=" ")
print()
print("--------------------")

i = 0
while i <= 12:
    print(i, end=" ")
    i += 1
print()
print("--------------------")

i = 0
while i <= 12:
    print(i, end=" ")
    if i == 5:
        break
    i += 1
