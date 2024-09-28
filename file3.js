function checkInput(value) {
    let result = '';

    if (value === null) {
        result = 'Input is null';
    } else if (typeof value === 'undefined') {
        result = 'Input is undefined';
    } else if (typeof value === 'string') {
        if (value.length === 0) {
            result = 'Input is an empty string';
        } else if (value.length < 5) {
            result = 'Input string is too short';
        } else if (value.length > 20) {
            result = 'Input string is too long';
        } else {
            result = 'Input is a valid string';
        }
    } else if (typeof value === 'number') {
        if (value < 0) {
            result = 'Input is a negative number';
        } else if (value === 0) {
            result = 'Input is zero';
        } else if (value > 100) {
            result = 'Input is greater than 100';
        } else {
            result = 'Input is a valid number';
        }
    } else if (Array.isArray(value)) {
        if (value.length === 0) {
            result = 'Input is an empty array';
        } else {
            result = 'Input is a valid array';
        }
    } else {
        result = 'Input type is not recognized';
    }

    return result;
}

// Example usage
console.log(checkInput(null));            // Input is null
console.log(checkInput(undefined));       // Input is undefined
console.log(checkInput(""));              // Input is an empty string
console.log(checkInput("abc"));           // Input string is too short
console.log(checkInput("This is a long string that exceeds twenty characters")); // Input string is too long
console.log(checkInput(50));              // Input is a valid number
console.log(checkInput(-10));             // Input is a negative number
console.log(checkInput(0));               // Input is zero
console.log(checkInput(150));             // Input is greater than 100
console.log(checkInput([]));              // Input is an empty array
console.log(checkInput([1, 2, 3]));      // Input is a valid array
console.log(checkInput({}));              // Input type is not recognized
