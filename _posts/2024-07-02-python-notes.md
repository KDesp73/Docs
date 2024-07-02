---
title: Python Notes
date: 2024-07-02 10:43:00 +0200
categories: [notes]
tags: [python]
---

## Variables

```python
num = 5
s = "Example"
arr = [5, 2, 6, 2, 7]
b = False
```

## I/O

### Output

```python
print("Hello World") # Hello World
print("Hello", "Kostas") # Hello Kostas

print("num = ", num) # num = 5
```

### Input

```python
i = input("Enter a number: ")

# But i is not a number. It's a string. All input is initially text
# We can cast this to a number

i = int(i) # Now it's a number (integer)
```

## Blocks

### If

```python
age = int(input("Enter your age: "))

if age < 18:
  print("You are not old enough")
else:
  print("You are old enough")
```

```python
num = int(input("Enter a number: "))

if num < 0:
  print(f"{num} is negative") # this is called an f-string
elif num > 0:
  print(f"{num} is positive")
else:
  print(f"{num} is zero")
```

### While

```python
a = 5
while a > 0:
  print(a)
  a -= 1 # We remove 1 from a (a = a - 1)
```

Output:
```
5
4
3
2
1
```

### For

```python
for i in range(0, 10):
  print(i)
```

Output:

```
0
1
2
...
...
8
9
```

## Functions

Functions are blocks of code that can be executed whenever we want. They can take inputs and return an output

```python
def sum(x, y):
  return x + y


a = sum(6, 2)
print(a) # 8
```

```python
def method():
  print("This method does not take or return values")
  print("It just does stuff")

method() # This is how we call it
```
