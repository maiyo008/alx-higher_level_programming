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


