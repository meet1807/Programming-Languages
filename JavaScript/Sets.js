//The Set constructor lets you create Set objects that store unique values of any type

const set1 = new Set([1, 2, 3, 4, 5]);
let mySet = new Set();

// methods

// .add(element)
// .has(element)
// .clear()             => removes all elements
// .delete(value)       => delets the element and return true or false base on successful operation
// .size                => returns the size

// .keys()
// .values()
// .entries()           => returns the key, value pair

// Array.from(mySet)    => converts mySets to an array and returns it
// [...mySet]           => copies elements of mySet to an array

//Iterations:

// logs the items in the order: 1, "some text", {"a": 1, "b": 2}, {"a": 1, "b": 2}
// for (let item of mySet) console.log(item)

// logs the items in the order: 1, "some text", {"a": 1, "b": 2}, {"a": 1, "b": 2}
// for (let item of mySet.keys()) console.log(item)

// Use the regular Set constructor to transform an Array into a Set
let mySet = new Set(myArray);

// Use to remove duplicate elements from the array

const numbers = [2, 3, 4, 4, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 5, 32, 3, 4, 5];

console.log([...new Set(numbers)]);
