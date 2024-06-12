// Hoisting is a javascript default behaviour of moving declarations
// to the top of the current scope
// because of this, functions can be called before they are declared

myFunction(5);

function myFunction(y) {
    return y * y;
}

