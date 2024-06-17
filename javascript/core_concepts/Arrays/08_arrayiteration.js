#!/usr/bin/env node
// There are various ways to iterate through an array

// FOR EACH ()
// forEach() method calls a function(a call back function) once for each array element

const numbers = [45, 7, 9, 16, 67, 35];
let txt = "";
numbers.forEach(myFunction); //  Should take in three arguments

function myFunction(value, index, array) { // This a call back function
    txt += `Element at index ${index} is ${value}. Array: ${array}\n`
}

// Foreach calls myFunction after every loop
//console.log(txt);


// ARRAY MAP()
// Array map() method creates a new array by perfoming a function on each array element
// The map method does not execute the function for the arrays without values

const numbers1 = [457, 8939, 57, 28, 4413];
const numbers2 = numbers1.map(myFunc);

function myFunc(value) {
    return value * 2
}

console.log(numbers2); // Every element in numbers 1 is multiplied by 2
// then saved into numbers 2
// Output [ 914, 17878, 114, 56, 8826 ];



// ARRAY FLATMAP()
// The flatmap() method first maps all the elements of an
// Array, then creates a new array by flattening the array

const myArr = [1, 2, 3, 4, 5, 6];
const newArr = myArr.flatMap((x) => x * 2); // Arrow function used

console.log(newArr); // Elements in myArr are multiplied by two



// Array Filter()
// The filter method creates a new array with the array elements that pass a test


const ages = [56, 4, 7, 17, 35, 24, 18];
const over18 = numbers.filter(above18);

function above18(value) {
    return value > 18
} // Filtered values are saved in the over!8 as a new array

console.log(over18);