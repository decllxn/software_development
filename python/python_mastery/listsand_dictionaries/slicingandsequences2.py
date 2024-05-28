from lists_modules import integers

# you can slice and replace sliced part of a list

print(integers)

integers[3:7] = [99, 99, 99, 99]

print(integers)

# when you replace it with a list longer than the sliced part, list becomes longer

integers[3:7] = [101, 101, 101, 101, 101, 101] #it only needs 4 items
print(integers)

#And becomes shorter if you replace it with a shorter list

integers[3:7] = [10000001]


