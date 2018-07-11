"use strict";
// function foo(a) {
//   var b = a;
//   return a + b;
// }

// var c = foo(2);
// var d = foo(3);

// console.log(c);
// console.log(d);

// function foo(a) {
//   var b = a;
//   console.log("a + b", a + b);
//   return a + b;
// }

// console.log("foo", foo(2));

function init() {
  var name = "Mozilla"; // name is a local variable created by init
  function displayName() {
    // displayName() is the inner function, a closure
    alert(name); // use variable declared in the parent function
  }
  displayName();
}
init();
