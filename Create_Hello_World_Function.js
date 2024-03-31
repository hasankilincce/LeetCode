/**
 * @return {Function}
 */
var createHelloWorld = function() {
    return function(...args) {
        return "Hello World";
    }
};

// Test cases
const f = createHelloWorld();
console.log(f()); // Output: "Hello World"
