# 0x00. Pagination
## Resources

Read or watch:
- [REST API Design: Pagination](https://example.com)
- [HATEOAS](https://example.com)

## Learning Objectives

By the end of this project, you will be able to:
- Paginate a dataset with simple `page` and `page_size` parameters.
- Paginate a dataset with hypermedia metadata.
- Paginate in a deletion-resilient manner.

## Requirements

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7).
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Your code should use the `pycodestyle` style (version 2.5.*).
- The length of your files will be tested using `wc`.
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
- All your functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`).
- A documentation is not a simple word; it’s a real sentence explaining the purpose of the module, class, or method (the length of it will be verified).
- All your functions and coroutines must be type-annotated.

## Setup

Use the `Popular_Baby_Names.csv` data file for your project.

## Tasks

### 0. Simple helper function

Write a function named `index_range` that takes two integer arguments `page` and `page_size`.

The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.

Example:

```python
#!/usr/bin/env python3
"""
Main file
"""

index_range = __import__('0-simple_helper_function').index_range

res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)

# Output
<class 'tuple'>
(0, 7)
<class 'tuple'>
(30, 45)
