from Team.Fer.core.utils import oneSec

@oneSec
def print_something(something):
    print(something)


for i in range(10):
    print_something(i)
