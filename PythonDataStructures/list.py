fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# Methods with their respective examples

# list.append(x)  -> Add an item to the end of the list. Equivalent to a[len(a):] = [x].

fruits.append('hello')
fruits[len(fruits):] = ['meet']
print(fruits)

# list.extend(iterable) -> Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

anotherList = ["hold", "my", "beer"]
fruits.extend(anotherList)
#fruits[len(fruits):] = anotherList
print(fruits)

# list.insert(i, x) -> i is index before which to insert x. a.insert(len(a), x) is equivalent to a.append(x).

# list.remove(x) -> removes the first value whose value is x -> ValueError if no such item in list

# list.pop(i) -> [i] is optional. if provided removes the value at ith index otherwise from the end

# list.clear() -> removes all items form the list. -> del a[:]

# list.index(x [, start[, end]] ) -> returns the index of x -> ValueError is no such value
#                                 -> if start and/or end provided it searches the value of x in between

# list.count(x) -> Return the number of times x appears in the list.

# list.sort(*, key=None, reverse=False) -> sorts the list -> if reverse=True provided it sorts on descending order
#                                       -> if key is provided it sorts accordingly

# list.reverse() -> reverse the elemnet of the list in place

# list.copy() -> return shallow copy of the list  -> a[:]
