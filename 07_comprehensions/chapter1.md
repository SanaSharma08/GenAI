# Python Comprehensions in detail documentation
# All u need to read for revision! 

## Overview
Comprehensions are concise and efficient ways to create collections (lists, sets, dictionaries or generators) by transforming or filtering iterables (in a single line of code). They provide a more readable and Pythonic alternative to loops and `map()`/`filter()` functions.

---

## 1. List Comprehensions

### Basic Syntax
```python
[expression for item in iterable]
```

### Simple Example
```python
# Without comprehension
squares = []
for x in range(5):
    squares.append(x ** 2)
print(squares)  # [0, 1, 4, 9, 16]

# With comprehension
squares = [x ** 2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

### With Conditional (if)
```python
# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# Filter and transform
doubled_evens = [x * 2 for x in numbers if x % 2 == 0]
print(doubled_evens)  # [4, 8, 12, 16, 20]
```

### With Multiple Conditions
```python
numbers = range(1, 21)
result = [x for x in numbers if x % 2 == 0 if x % 3 == 0]
print(result)  # [6, 12, 18]
```

### Nested Comprehensions
```python
# Create a 3x3 matrix
matrix = [[x * y for x in range(1, 4)] for y in range(1, 4)]
print(matrix)
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Flatten a nested list
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for row in nested for item in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## 2. Set Comprehensions

### Basic Syntax
```python
{expression for item in iterable}
```

### Examples
```python
# Remove duplicates and transform
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_squares = {x ** 2 for x in numbers}
print(unique_squares)  # {1, 4, 9, 16}

# Filter and create set
words = ["apple", "banana", "cherry", "apricot", "blueberry"]
words_with_a = {word for word in words if 'a' in word}
print(words_with_a)  # {'apple', 'banana', 'apricot'}
```

---

## 3. Dictionary Comprehensions

### Basic Syntax
```python
{key_expression: value_expression for item in iterable}
```

### Examples
```python
# Create a mapping from numbers to their squares
squares_dict = {x: x ** 2 for x in range(5)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Transform a list into a dictionary
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)  # {'Alice': 5, 'Bob': 3, 'Charlie': 7}

# Filter and create dictionary
numbers = range(1, 11)
odd_squares = {x: x ** 2 for x in numbers if x % 2 == 1}
print(odd_squares)  # {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Swap keys and values
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}
```

---

## 4. Generator Expressions

### Basic Syntax
```python
(expression for item in iterable)
```

### Key Differences from List Comprehensions
- **Memory efficient**: Generates values on-the-fly instead of storing all in memory
- **Lazy evaluation**: Computes values only when needed
- **Syntax**: Uses parentheses `()` instead of square brackets `[]`

### Examples
```python
# List comprehension (stores all in memory)
squares_list = [x ** 2 for x in range(1000000)]

# Generator expression (lazy evaluation)
squares_gen = (x ** 2 for x in range(1000000))
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1
print(next(squares_gen))  # 4

# Use in loops
for square in (x ** 2 for x in range(5)):
    print(square)  # 0, 1, 4, 9, 16

# Use with built-in functions
numbers = range(1, 11)
total = sum(x ** 2 for x in numbers)
print(total)  # 385
```

---

## 5. Comparison: Traditional vs Comprehensions

### List Example
```python
# Traditional way (verbose)
result = []
for x in range(10):
    if x % 2 == 0:
        result.append(x * 2)
print(result)  # [0, 2, 4, 6, 8, 12, 14, 16, 18]

# Comprehension way (concise)
result = [x * 2 for x in range(10) if x % 2 == 0]
print(result)  # [0, 2, 4, 6, 8, 12, 14, 16, 18]
```

---

## 6. Real-World Examples

### Extract file extensions
```python
files = ["document.pdf", "image.png", "script.py", "music.mp3"]
extensions = {file.split('.')[-1] for file in files}
print(extensions)  # {'pdf', 'png', 'py', 'mp3'}
```

### Create a frequency counter
```python
sentence = "hello world"
char_count = {char: sentence.count(char) for char in set(sentence)}
print(char_count)  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```

### Filter dictionary
```python
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}
high_scorers = {name: score for name, score in scores.items() if score >= 90}
print(high_scorers)  # {'Bob': 92, 'Diana': 95}
```

### Flatten nested structures
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## 7. Benefits of Comprehensions

| Benefit | Description |
|---------|-------------|
| **Readability** | More Pythonic and easier to read than loops |
| **Performance** | Faster than equivalent loops (optimized in CPython) |
| **Conciseness** | Reduces code length significantly |
| **Functional Style** | Encourages functional programming paradigms |
| **Memory Efficiency** | Generators avoid storing entire collections |

---

## 8. When to Use Comprehensions

✅ **Use comprehensions when:**
- Creating new collections from existing ones
- Performing simple transformations
- Filtering elements
- The logic is simple and fits on one or two lines

❌ **Avoid comprehensions when:**
- The logic is complex (use loops for clarity)
- Multiple operations are needed (nested comprehensions become unreadable)
- Side effects are involved (e.g., modifying external state)

---

## 9. Summary

| Type | Syntax | Use Case |
|------|--------|----------|
| **List Comp.** | `[expr for x in iter]` | Create filtered/transformed lists |
| **Set Comp.** | `{expr for x in iter}` | Create sets with unique elements |
| **Dict Comp.** | `{k: v for x in iter}` | Create dictionaries |
| **Generator** | `(expr for x in iter)` | Memory-efficient iteration |

Comprehensions are a powerful feature of Python that make code more readable and efficient. Master them to write more Pythonic code!