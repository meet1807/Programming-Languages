// Do not confuse the "primitive Boolean values true and false with the true and false values of the Boolean object".

//Example 1
let x = new Boolean(false); // new creates an object of Boolean class and passes "false" as value to it's constructor
if (x) {
  console.log(x);
  // this code is executed
}

//Example 2
var a = false;
if (a) {
  // this code is not executed
}

var b = Boolean(expression); // use this...   calls the class
var c = !!expression; // ...or this
var d = new Boolean(expression); // don't use this!   creates an object of a class and passes the value to it's constructor function

//falsy values
