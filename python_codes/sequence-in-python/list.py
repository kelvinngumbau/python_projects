#list in python
#list is defined using square brackets
numbers = [10,23,45,65,75,78,90]
names = ['kelvin','madisson','Maguire','Harry','Shaw','Rashford']
mixed  = [10,25,45,65,'Degea','David','Luke','Kovacic']
#accessing values
print(numbers)
print(names)
print(mixed)
print(numbers[0])
print(names[0:5])
print(numbers[:5])
print(numbers[1:])
#modifying elements
numbers[0] = 20
print(numbers)

#list operations
combine = numbers + names
print(combine)

#list functions
print(len(numbers))
print(len(names))
print(max(numbers))
print(min(names))
print(list(names))
#list methods
#list.append(x), appends element to the list
print(numbers.append(99))
print(numbers)
#list.count(x), counts how many times an elementappear in the list
print(numbers.count(99))

#list.index(x), returns the first index at which the element occurs in the list
print(numbers.index(99))

#list.pop, removes and returns last element
print(names.pop())

#list.reverse, reverse the order of the elements
print(names.reverse())
print(names)