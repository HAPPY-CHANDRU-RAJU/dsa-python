# Python Strings

## Introduction

In Python, a string is an immutable sequence of characters. Strings are used to store and manipulate text data.

## Creating Strings

You can create strings using single quotes `'`, double quotes `"`, or triple quotes `'''` or `"""` for multi-line strings.

```python
# Creating strings
single_quote_string = 'Hello, World!'
double_quote_string = "Hello, World!"
multi_line_string = """This is a
multi-line string."""
```

## Accessing Characters

You can access individual characters in a string using indexing.

```python
# Accessing characters
first_char = single_quote_string[0]  # 'H'
last_char = single_quote_string[-1]  # '!'
```

## Slicing Strings

You can slice strings to obtain substrings.

```python
# Slicing strings
substring = single_quote_string[0:5]  # 'Hello'
```

## String Concatenation and Repetition

You can concatenate and repeat strings using `+` and `*` operators.

```python
# Concatenation
greeting = "Hello, " + "World!"  # 'Hello, World!'

# Repetition
repeat_string = "Hi! " * 3  # 'Hi! Hi! Hi! '
```

## Useful String Methods

Python provides several built-in methods for string manipulation.

- `strip()`: Removes leading and trailing whitespace.
- `lstrip()`: Removes leading whitespace.
- `rstrip()`: Removes trailing whitespace.
- `lower()`: Converts all characters to lowercase.
- `upper()`: Converts all characters to uppercase.
- `title()`: Converts the first character of each word to uppercase.
- `capitalize()`: Converts the first character to uppercase and the rest to lowercase.
- `find(sub)`: Returns the lowest index of the substring `sub`. Returns `-1` if not found.
- `rfind(sub)`: Returns the highest index of the substring `sub`. Returns `-1` if not found.
- `replace(old, new)`: Replaces occurrences of substring `old` with `new`.
- `split(delimiter)`: Splits the string into a list using `delimiter`.
- `join(iterable)`: Joins elements of an iterable into a string using the string as a separator.
- `splitlines()`: Splits the string at line breaks.
- `format(*args, **kwargs)`: Formats the string using placeholders.
- `isupper()`: Checks if all characters in the string are uppercase.
- `islower()`: Checks if all characters in the string are lowercase.
- `istitle()`: Checks if the string is in title case (i.e., first character of each word is uppercase).
- `isspace()`: Checks if all characters in the string are whitespace.
- `isalpha()`: Checks if all characters in the string are alphabetic.
- `isdigit()`: Checks if all characters in the string are digits.
- `isalnum()`: Checks if all characters in the string are alphanumeric (letters and numbers).

```python
# Example of string methods
text = "  Hello, World!  "

# Strip whitespace from both ends
stripped_text = text.strip()  # 'Hello, World!'

# Strip leading whitespace
lstripped_text = text.lstrip()  # 'Hello, World!  '

# Strip trailing whitespace
rstripped_text = text.rstrip()  # '  Hello, World!'

# Convert to lowercase
lower_text = text.lower()  # '  hello, world!  '

# Convert to uppercase
upper_text = text.upper()  # '  HELLO, WORLD!  '

# Capitalize
capitalized_text = text.capitalize()  # '  hello, world!  '

# Find a substring
index = text.find("World")  # 7

# Replace a substring
replaced_text = text.replace("World", "Python")  # '  Hello, Python!  '

# Split the string
split_text = text.split(",")  # ['  Hello', ' World!  ']

# Join a list into a string
joined_text = "-".join(['2024', '09', '09'])  # '2024-09-09'

# Split lines
lines = "line1\nline2\nline3".splitlines()  # ['line1', 'line2', 'line3']

# Format a string
formatted_text = "Hello, {}!".format("Python")  # 'Hello, Python!'

# Check if all characters are uppercase
is_upper = "HELLO".isupper()  # True

# Check if all characters are lowercase
is_lower = "hello".islower()  # True

# Check if the string is in title case
is_title = "Hello World".istitle()  # True

# Check if all characters are whitespace
is_space = "   ".isspace()  # True

# Check if all characters are alphabetic
is_alpha = "Hello".isalpha()  # True

# Check if all characters are digits
is_digit = "123".isdigit()  # True

# Check if all characters are alphanumeric
is_alnum = "Hello123".isalnum()  # True
```

## String Formatting

String formatting allows you to create strings with variable content.

- **Old-style formatting** using `%` operator.
- **New-style formatting** using `str.format()`.
- **F-strings** (formatted string literals) in Python 3.6+.

```python
# Old-style formatting
name = "Alice"
age = 30
old_style = "Name: %s, Age: %d" % (name, age)  # 'Name: Alice, Age: 30'

# New-style formatting
new_style = "Name: {}, Age: {}".format(name, age)  # 'Name: Alice, Age: 30'

# F-strings (Python 3.6+)
f_string = f"Name: {name}, Age: {age}"  # 'Name: Alice, Age: 30'
```

## Escape Sequences

Escape sequences are used to insert special characters in strings.

```python
# Escape sequences
escaped_string = "Line1\nLine2\tTabbed"  # 'Line1\nLine2\tTabbed'
```

## Raw Strings

Raw strings treat backslashes as literal characters, useful for regular expressions and file paths.

```python
# Raw string
raw_string = r"C:\Users\Name\Documents"  # 'C:\\Users\\Name\\Documents'
```

## Multiline Strings

Multiline strings can be created with triple quotes.

```python
# Multiline string
multi_line_string = """This is a string
that spans multiple lines."""
```

## String Length

To get the length of a string (i.e., the number of characters it contains), use the `len()` function.

```python
text = "Hello, World!"
length = len(text)  # 13
```

## Checking Substrings

You can check if a substring exists within a string using `in` or `not in`.

```python
text = "Hello, World!"
contains_hello = "Hello" in text  # True
contains_python = "Python" not in text  # True
```

## String Membership

Check if a string starts or ends with a specific substring using `startswith()` and `endswith()`.

```python
text = "Hello, World!"
starts_with_hello = text.startswith("Hello")  # True
ends_with_world = text.endswith("World!")  # True
```

## String Repetition

Repeat a string multiple times using the `*` operator.

```python
text = "Hi! "
repeated_text = text * 3  # 'Hi! Hi! Hi! '
```

## String Concatenation

Concatenate strings using the `+` operator.

```python
greeting = "Hello, "
name = "Alice"
full_greeting = greeting + name  # 'Hello, Alice'
```

## String Splitting

Split a string into a list of substrings using the `split()` method.

```python
text = "apple,banana,cherry"
split_text = text.split(",")  # ['apple', 'banana', 'cherry']
```

## String Joining

Join a list of strings into a single string using the `join()` method.

```python
words = ['Python', 'is', 'fun']
sentence = " ".join(words)  # 'Python is fun'
```

## String Finding

Find the index of the first occurrence of a substring using `find()` and the last occurrence using `rfind()`. They return `-1` if the substring is not found.

```python
text = "Hello, World!"
index_first = text.find("World")  # 7
index_last = text.rfind("o")  # 8
```

## Conclusion

String operations in Python provide powerful ways to manipulate and interact with text data. Mastering these operations will enhance your ability to process and analyze strings effectively.
