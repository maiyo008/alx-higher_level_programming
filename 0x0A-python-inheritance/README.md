# 0x0A. Python - Inheritance
---
## Objectives
---
* What is a superclass, baseclass or parentclass
* What is a subclass
* How to list all attributes and methods of a class or instance
* When can an instance have new attributes
* How to inherit class from another
* How to define a class with multiple base classes
* What is the default class every class inherit from
* How to override a method or attribute inherited from the base class
* Which attributes or methods are available by heritage to subclasses
* What is the purpose of inheritance
*What are, when and how to use `isinstance`, `issubclass`, `type` and `super` built-in functions
---
## Resources
---
*[Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
* [Multiple inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
* [Inheritance in Python](https://www.geeksforgeeks.org/inheritance-in-python/)
* [Learn to Program 10 : Inheritance Magic Methods](https://www.youtube.com/watch?v=d8kCdLCi6Lk)
---
## Tasks
---
### Task 0
* Write a function that returns the list of available attributes and methods of an object:
	* Prototype: `def lookup(obj):`
	* Returns a `list` object
	* You are not allowed to import any module

### Task 1
* Write a class `MyList` that inherits from `list`:
	* Public instance method: `def print_sorted(self)`: that prints the list, but sorted (ascending sort)
	* You can assume that all the elements of the list will be of type `int`
	* You are not allowed to import any module

### Task 2
* Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False
	* Prototype: `def is_same_class(obj, a_class): `
	* You are not allowed to import any module

### Task 3
* Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.
	* Prototype: `def is_kind_of_class(obj, a_class):`
	* You are not allowed to import any module

### Task 4
* Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.
	* Prototype: `def inherits_from(obj, a_class):`
	* You are not allowed to import any module

### Task 5
* Write an empty class `BaseGeometry`
	* You are not allowed to import any module


### Task 6
* Write a class `BaseGeometry`(based on [5-base_geometry.py](https://github.com/maiyo008/alx-higher_level_programming/blob/main/0x0A-python-inheritance/5-base_geometry.py)
	* Public instance method: `def area(self)`:  that raises an exception with the message `area() is not implemented`
	* You are not allowed to import any module

### Task 7
*  Write a class `BaseGeometry`(Based on [6-base_geometry.py](https://github.com/maiyo008/alx-higher_level_programming/blob/main/0x0A-python-inheritance/6-base_geometry.py))
	* Public instance method: `def area(self):`   that raises an `Exception` with the message  `area() is not implemented`
	* Public instance method: `def integer_validator(self, name, value): that validates `value`.
		* you can assume `name` is always a string
		* if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
		* if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
	* You are not allowed to import any module

### Task 8
* Write a class `Rectangle` that inherits from `BaseGeometry`([7-base_geometry.py](https://github.com/maiyo008/alx-higher_level_programming/blob/main/0x0A-python-inheritance/7-base_geometry.py))
	* Instantiation with `width` and `height`: `def __init__(self, width, height):`
		* `width` and `height` must be private. No getter or setter
		* `width` and `height` must be positive integers, validated by `integer_validator`

### Task 9
* Write a class `Rectangle` that inherits from `BaseGeometry` (Based on [7-base_geometry.py](https://github.com/maiyo008/alx-higher_level_programming/blob/main/0x0A-python-inheritance/7-base_geometry.py))
	* Instantiation with `width` and `height`: `height: def __init__(self, width, height):`
		* `width` and `height` must be private. No getter or setter
		* `width` and `height` must be positive integers validated by `integer_validator`
* The `area()` method must be implemented
* `print()` should print,  and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`

### Task 10
* Write a class `Square` that inherits from `Rectangle` (Based on [9-rectangle.py](https://github.com/maiyo008/alx-higher_level_programming/blob/main/0x0A-python-inheritance/9-rectangle.py))
	* Instantiation with `size: def __init__(self, size):`
		* `size` must be private. No getter no Setter
		* `size` must be a positive integer, validated by `integer_validator`
	* The area must be implemented

### Task 11
* Write a class `Square` that inherits from `Rectangle`. (Based on [10-square.py](https://github.com/maiyo008/alx-higher_level_programming/blob/main/0x0A-python-inheritance/10-square.py))
	* Instantiation with `size: def __init__(self, size):`                                                                       * `size` must be private. No getter no Setter                                                                        * `size` must be a positive integer, validated by `integer_validator`                                        * The area must be implemented 
	* `print()` should print, and `str()` should return the square description: `[Square] <width>/<height>`

  
