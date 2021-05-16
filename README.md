# Python_Introduction

In this repository I have used different basic concepts of python

**List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list**.

Syntax:
```
newlist = [expression for item in iterable if condition == True]
```
**A lambda function is a small anonymous function.A lambda function can take any number of arguments, but can only have one expression.**

Syntax:
```
lambda arguments : expression
```
# Inheritance

**Inheritance allows us to define a class that inherits all the methods and properties from another class.Parent class is the class being inherited from, also called base class.Child class is the class that inherits from another class, also called derived class.**

Syntax:
```
class A():
    pass
class B(A):
    pass
```
# Encapsulation

**Using OOP in Python, we can restrict access to methods and variables. This prevents data from direct modification which is called encapsulation. In Python, we denote private attributes using underscore as the prefix i.e single _ or double __.**

# Polymorphism

**Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle). However we could use the same method to color any shape. This concept is called Polymorphism.**

# Opening a File
---
File Open Mode | Description
---------------|------------
<<<<<<< HEAD
w | To write data into file. If any data is already present in the file, it would be deleted and the present   data will be stored
 r | To read data from the file. The file pointer is positioned at the beginning of the file.
a | To append data to the file. It adds to the end of file. If file doesnot exist, it will create a new file 
    for writing data.
=======
w | To write data into file. If any data is already present in the file, it would be deleted and the present data will be stored
r | To read data from the file. The file pointer is positioned at the beginning of the file.
a | To append data to the file. It adds to the end of file. If file doesnot exist, it will create a new file for writing data.
>>>>>>> 3ba0629f5f83c965fdf84312ed29a3be37e5c5bf
w+ | To write and read data of a file. The previous data in the file will be deleted.
r+ | To read and write data into a file. The previous data in the file will not be deleted. The file pointer is placed at the beginning of the file.
a+ | To append and read data of a file. The file pointer will be at the end of the file if the file exists.The file pointer will be at the end of the file if the file exists. If      the file doesnot exist, It creates a new file for reading and writing.
