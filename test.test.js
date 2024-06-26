// Test case 1: Adding a number
calculator.add(5);
console.log(calculator.getValue()); // Output: 5

// Test case 2: Subtracting a number
calculator.subtract(2);
console.log(calculator.getValue()); // Output: 3

// Test case 3: Multiplying by a number
calculator.multiply(3);
console.log(calculator.getValue()); // Output: 9

// Test case 4: Dividing by a non-zero number
calculator.divide(4);
console.log(calculator.getValue()); // Output: 2.25

// Test case 5: Dividing by zero
calculator.divide(0);
console.log(calculator.getValue()); // Output: Error: Cannot divide by zero