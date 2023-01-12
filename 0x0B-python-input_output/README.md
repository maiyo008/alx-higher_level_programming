# 0x0B. Python - Inputs and Outputs
----
## Learning objectives
----
* How to open a file
* How to write text in a file
* How to read the full content of a file
* How to read a file line by line
* How to move the cursor in a file
* How to make sure a file is closed after using it
* What is and how to use the `with` statement
* What is `JSON`
* What is serialization
* What is deserialization
* How to convert a Python data structure to a JSON string
* How to convert a JSON string to a Python data structure
---
## Tasks
---
### Task 0
* Write a function that reads a text file (UTF8) and prints it to stdout:
	* Prototype: `def read_file(filename=""):`
	* You must use the `with` statement
	* You don't need to manage `file permission` or `file does't exists` exceptions
	* You are not allowed to import any module

### Task 1
* Write a function that writes a string to a text file (UTF8) and returns the number of characters written:
	* Prototype: `def write_file(filename="", text="")`
	* You must use the `with` statement
	* You don’t need to manage file permission exceptions.
	* Your function should create the file if doesn’t exist.
	* Your function should overwrite the content of the file if it already exists.
	* You are not allowed to import any module


