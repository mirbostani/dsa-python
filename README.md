# DSA-Python

Data Structures and Algorithms in Python

## Table of Contents

- [Stack](./src/stack/)
  - [x] [Stack with Dynamic Array](./src/stack/stack_with_dynamic_array.py)
  - [x] [Stack with Linked List](./src/stack/stack_with_linked_list.py)
  - [x] [Stack with Fixed-Size Array](./src/stack/stack_with_fixed_size_array.py)
  - Examples
    - [x] [Reverse String](./src/stack/examples/reverse_string.py)
    - [x] [Match Parentheses](./src/stack/examples/match_parentheses.py)
- [Queue](./src/queue/)
  - Simple Queue
    - [x] [Queue with Dynamic Array](./src/queue/queue_with_dynamic_array.py)
    - [x] [Queue with Fixed-Size Array](./src/queue/queue_with_fixed_size_array.py)
    - [x] [Queue with Two Stacks](./src/queue/queue_with_two_stacks.py)
  - Circular Queue
  - Priority Queue
  - Double Ended Queue

## Test

Executing a single `*_test.py` file:

```bash
$ python3 -m unittest ./src/stack/test/*_test.py -v
```

Executing all the test files:

```bash
$ python3 -m unittest discover -p "*_test.py" -v 
```