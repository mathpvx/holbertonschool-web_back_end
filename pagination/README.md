# Pagination

## Requirements
- All the files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7)
- All the files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5.*)
- The length of the files will be tested using `wc`
- All the modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All the functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class, or method (the length of it will be verified)
- All the functions and coroutines must be type-annotated.

## Tasks Examples

### Task 0: Simple helper function

Write a function named `index_range` that takes two integer arguments `page` and `page_size`.

The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.

### Task 1: Simple pagination

Copy index_range from the previous task and the following class into your code

Implement a method named get_page that takes two integer arguments page with default value 1 and page_size with default value 10.

You have to use this CSV file (same as the one presented at the top of the project)
Use assert to verify that both arguments are integers greater than 0.
Use index_range to find the correct indexes to paginate the dataset correctly and return the appropriate page of the dataset (i.e. the correct list of rows).
If the input arguments are out of range for the dataset, an empty list should be returned.
