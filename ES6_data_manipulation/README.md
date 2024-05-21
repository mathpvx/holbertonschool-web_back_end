# ES6 Data Manipulation

This project focuses on enhancing our skills with ES6 features for data manipulation in JavaScript. Here we learn to efficiently manipulate data using modern array methods (`map`, `filter`, `reduce`), explore the usage of typed arrays, and understand advanced data structures like `Set`, `Map`, and `WeakMap`.

## Requirements
- All the files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
- Allowed editors: `vi`, `vim`, `emacs`, Visual Studio Code
- All the files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- The code should use the `.js` extension
- The code will be tested using Jest and the command `npm run test`
- The code will be verified against lint using ESLint
- The code needs to pass all the tests and lint. You can verify the entire project running `npm run full-test`
- All of the functions must be exported

## Tasks Examples

### 0. Basic list of objects

Create a function named getListStudents that returns an array of objects.

Each object should have three attributes: id (Number), firstName (String), and location (String).

The array contains the following students in order:

Guillaume, id: 1, in San Francisco
James, id: 2, in Columbia
Serena, id: 5, in San Francisco

### 8. Clean set

Create a function named cleanSet that returns a string of all the set values that start with a specific string (startString).

It accepts two arguments: a set (Set) and a startString (String).

When a value starts with startString you only append the rest of the string. The string contains all the values of the set separated by -.

Author : Mathilde Pavaux
