# 0x0C. Python - Almost a circle
------
## Objectives
-----
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* What is `*args` and how to use it
* What is `**kwargs` and how to use it
* How to handle named arguments in a function
------
## Resources
------
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
* [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
----
## Tasks
-----
### Task 0
* All your files, classes and methods must be unit tested and be PEP 8 validated. 

### Task 1
* Write the first class `Base`:
* Create a folder named `models` with an empty file `__init__.py`inside - with this file, the folder will become a Python package
* Create a file named `models/base.py`:
	* Class `Base`:
		* Private class attribute `__nb_objects = 0
		* class constructor: `def __init__(self, id=None)`:
			* if `id` is not `None`, assign a public instance attribute `id` with this argumentargument value - you can assume id is an integer and you don’t need to test the type of it
			* Otherwise, increment `__nb_objects` and assign the new value to the public instance attribute `id`
* This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)

### Task 2
* Write a class `Rectangle` that inherits from `Base`:
	* In the file `models/rectangle.py`
	* Class `Rectangle` inherits from `Base`
	* Private instance attributes, each with its own public getter and setter:
		* `__width` -> `width`
		* `__height`-> `height`
		* `__x` -> `x`
		* `__y` -> `y`
* Class constructor `def __init__(self, width, height, x=0, y=0, id=None):
	* Call the super class with `id` - this super call with use the logic of the  `__init__` of the `Base` class
	* Assign each argument `width`, `height`, `x`, and `y` to the right attribute
* Why private attributes with getter/setter? Why not directly public attribute?
* Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can “trust” these attributes

### Task 3
* Update the class `Rectangle` by adding validation of all setter methods and instantiation (`id` excluded): 
	* If the input is not an integer, raise the `TypeError` exception with the message: `<name of the attribute> must be an integer`. Example: `width must be an integer`
	* If `width` or `height` is under or equals 0, raise the `ValueError` exception with the message: `<name of the attribute> must be > 0`. Example: `width must be > 0`
	* If `x` or `y` is under 0, raise the `ValueError` exception with the message: `<name of the attribute> must be >= 0`. Example: `x must be >= 0`

### Task 4
* Update the class `Rectangle`  by adding a public method `def area(self)`: that returns the value error of the `Rectangle` instance

### Task 5
* Undate class `Rectangle` by adding the public method `def display(self)`: that prints in the stdout the instance
with the character # - you don't need to handle `x` and `y` here.

### Task 6
* Update the class `Rectangle` by overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`

### Task 7
* Update the class `Rectangle` by improving the public method `def display(self)`: to print in the stdout the `Rectangle` instance with the character `#` by taking care of x and y

### Task 8
* Update the class `Rectangle` by adding the public method `def update(self, *args)`: that assigns an argument to each attribute:
	* 1st argument should be the `id` attribute
	* 2nd argument should be the `width` attribute
	* 3rd argument should be the `height` attribute
	* 4th argument should be the `x` attribute
	* 5th argument should be the `y` attribute
* This type of argument is called a “no-keyword argument” - Argument order is super important.

### Task 9
* Update the class `Rectangle`  by updating the public method `def update(self, *args):` by changing this prototype to `update(self, *args, **kwargs)` that assigns a key/value argument to the attributes
	* `**kwargs` can be  thought of as a double pointer to a dictionary: key/value
		* As Python doesn't have pointers, `**kwargs` is not literally a double pointer – describing it as such is just a way of explaining its behavior in terms you’re already familiar with
	* `**kwargs` must be skipped if `*args` exists and is not empty
	* Each key in this dictionary represents an attribute to the instance

### Task 10
* Write the class `Square` that inherits from `Rectangle:`
	* In the file `models/square.py`
	* Class `Square` inherits from `Rectangle`
	* Class Constructor: `def __init__(self, size, x=0, y=0, id=None):`:
		* Call the super class with `id`, `x`, `y`, `width` and `height` - this super call will use the logic of the `__init__` of the Rectangle class. The width and height must be assigned to the value of size
		* You must not create new attributes for this class, use all attributes of Rectangle - As reminder: a Square is a Rectangle with the same width and height
		* All `width`, `height`, `x` and `y` validation must inherit from `Rectangle` - same behavior in case of wrong data
	* The overloading `__str__` method should return `[Square] (<id>) <x>/<y> - <size>` - in our case, width or height
* As you know, a Square is a special Rectangle, so it makes sense this class Square inherits from Rectangle. Now you have a Square class who has the same attributes and same methods.

### Task 11
* Update the class `Square` by adding the public getter and setter `size`
	* The setter should assign (in this order) the `width` and the `height` - with the same value
	* The setter should have the same value validation as the `Rectangle` for `width` and `height` - No need to change the exception error message (It should be the one from `width`)

### Task 12
* Update the class `Square` by adding the public method `def update(self, *args, **kwargs)` that assigns the attribute
	* `*args` is the list of arguments - no-keyworded arguments
		* 1st argument should be the `id` attribute
		* 2nd argument should be the `size` attribute
		* 3rd argument should be the `x` attribute
		* 4th argument should be the `y` attribute
	* `**kwargs` can be thought of as a double pointer to a dictionary: key/value (keyworded arguments)
	* `**kwargs` must be skipped if `*args` exists and is not empty
	* Each key in this dictionary represents an attribute to the instance


