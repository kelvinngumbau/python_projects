#sets
#duplicates not allowed
#they are unordered and cannot be changed
myset = {'Rashford','Marcus','cucurella','Courtois','Vinicius','Rodrigo','Rodri','Casemiro','Dean'}
print(myset)
#nb true and 1 are considered the same value and are treated as a duplicate.
set2 = {True,1,5,'shaw'}
print(set2)
#len
print(len(set2))
print(type(set2))

for x in set2:
    print(x)

#searching if an element exists in a set
if 'shaw' in set2:
    print("shaw is present")
else:
    print("Shaw is not present")

#we can use set() constructor to create a set
set3 = set(('Greenwood','Mason','Foden','Walker','Phillips','Mount','South Gate','pep'))
print(set3)

#we can add a new element into a list but we cannot change the elements
#use add() method

n2 = set3.add('Martinez')
print(set3)

#to remove an item use remove() method
set3.remove('Martinez')
print(set3)

#joining two sets use update or union method
#note both methods will exclude any duplicates if any exists

n3 = set2.union(set3)
print(n3)

#use update
n4 = set3.update(myset)
print(n4)