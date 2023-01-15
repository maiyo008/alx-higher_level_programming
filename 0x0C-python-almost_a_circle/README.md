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
