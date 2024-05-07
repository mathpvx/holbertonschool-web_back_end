# ES6 Basics

## Requirements
General
- All the files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
- Allowed editors: vi, vim, emacs, Visual Studio Code
- All the files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- The code should use the js extension
- The code will be tested using the Jest Testing Framework
- The code will be analyzed using the linter ESLint along with specific rules that we’ll provide
- All of your functions must be exported

## Setup
### Install NodeJS 12.11.x
(in your home directory):

```bash
curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
nodejs -v
npm -v
```

## Tasks Examples
### 1. Block Scope
Given what you’ve read about var and hoisting, modify the variables inside the function taskBlock so that the variables aren’t overwritten inside the conditional block.
```
export default function taskBlock(trueOrFalse) {
  var task = false;
  var task2 = true;

  if (trueOrFalse) {
    var task = true;
    var task2 = false;
  }

  return [task, task2];
}
```
### 12. Let's create a report object
Write a function named createReportObject whose parameter, employeesList, is the return value of the previous function createEmployeesObject.

export default function createReportObject(employeesList) {

}
createReportObject should return an object containing the key allEmployees and a method property called getNumberOfDepartments.

allEmployees is a key that maps to an object containing the department name and a list of all the employees in that department. If you’re having trouble, use the spread syntax.

The method property receives employeesList and returns the number of departments. I would suggest suggest thinking back to the ES6 method property syntax.
```
{
  allEmployees: {
     engineering: [
          'John Doe',
          'Guillaume Salva',
     ],
  },
};
```
