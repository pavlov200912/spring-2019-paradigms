#!/usr/bin/env python3

my_range = range(5)
print(my_range)
for i in my_range:
    print(i)

iterator = iter(my_range)
# iterator = my_range.__iter__()
print(iterator)

v0 = next(iterator)
# v0 = iterator.__next__()
print(v0)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

print(my_range[5])
