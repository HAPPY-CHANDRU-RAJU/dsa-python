# Python Dictionaries

## Introduction

In Python, a dictionary is a mutable, unordered collection of key-value pairs. Each key must be unique and immutable (e.g., strings, numbers, tuples), while values can be of any type.

## Creating Dictionaries

You can create dictionaries using curly braces `{}` with key-value pairs separated by colons.

```python
# Creating a dictionary with integer keys
person = {1: "Alice", 2: "Bob", 3: "Charlie"}

# Creating a dictionary with string keys
employee = {"name": "John", "age": 30, "position": "Developer"}

# Creating an empty dictionary
empty_dict = {}
```

## Accessing Values

Values in a dictionary are accessed using their corresponding keys.

```python
# Accessing values by key
name = employee["name"]  # "John"
position = employee["position"]  # "Developer"
```

## Adding and Modifying Entries

You can add new key-value pairs or modify existing ones.

```python
# Adding a new key-value pair
employee["salary"] = 50000

# Modifying an existing value
employee["age"] = 31
```

## Removing Entries

You can remove key-value pairs using methods or the `del` statement.

```python
# Removing a key-value pair using del
del employee["position"]

# Removing a key-value pair using pop
salary = employee.pop("salary")  # 50000

# Removing the last inserted key-value pair using popitem
last_item = employee.popitem()  # (key, value) e.g., ("age", 31)
```

## Useful Methods

- `get(key, default=None)`: Returns the value for `key` if `key` is in the dictionary, else `default`.
- `keys()`: Returns a view object of all the keys.
- `values()`: Returns a view object of all the values.
- `items()`: Returns a view object of all the key-value pairs.
- `update(other_dict)`: Updates the dictionary with key-value pairs from another dictionary.
- `clear()`: Removes all key-value pairs from the dictionary.
- `copy()`: Returns a shallow copy of the dictionary.

```python
# Example of dictionary methods
person = {"name": "Alice", "age": 25, "city": "New York"}

# Using get method
name = person.get("name")  # "Alice"
age = person.get("age", 30)  # 25 (default is ignored)

# Using keys, values, and items
keys = person.keys()  # dict_keys(['name', 'age', 'city'])
values = person.values()  # dict_values(['Alice', 25, 'New York'])
items = person.items()  # dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

# Updating the dictionary
person.update({"country": "USA", "age": 26})

# Clearing the dictionary
person.clear()  # {}
```

## Dictionary Comprehensions

You can create dictionaries using dictionary comprehensions.

```python
# Creating a dictionary with comprehension
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Conditional dictionary comprehension
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

## Nested Dictionaries

Dictionaries can contain other dictionaries, creating a nested structure.

```python
# Creating a nested dictionary
contacts = {
    "Alice": {"phone": "123-456-7890", "email": "alice@example.com"},
    "Bob": {"phone": "987-654-3210", "email": "bob@example.com"}
}

# Accessing nested dictionary values
alice_email = contacts["Alice"]["email"]  # "alice@example.com"
```

## Iterating Over Dictionaries

You can use loops to iterate over keys, values, or key-value pairs.

```python
# Iterating over keys
for key in person:
    print(key)

# Iterating over values
for value in person.values():
    print(value)

# Iterating over key-value pairs
for key, value in person.items():
    print(key, value)
```

## Dictionary Operations

Dictionaries support various operations for combining and modifying data.

```python
# Merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = {**dict1, **dict2}  # {"a": 1, "b": 3, "c": 4}

# Copying a dictionary
copy_dict = dict1.copy()  # {"a": 1, "b": 2}
```

## Conclusion

Dictionaries are a versatile and powerful data structure in Python, useful for managing and accessing key-value pairs. Mastering their methods and features will enhance your ability to work with complex data.
