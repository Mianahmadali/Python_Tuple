# What is a tuple in Python?

# Explain the key differences between a tuple and a list in Python.


"""
A tuple in Python is a built-in data type that is used to store an ordered collection of items. Tuples are similar to lists, but they have some key differences. A tuple is defined by enclosing its elements in parentheses () instead of square brackets [], which are used for lists.

Example of a Tuple:

my_tuple = (1, 2, 3, "hello", 4.5)
Key Differences Between a Tuple and a List
Mutability:

Tuple: Immutable, meaning once a tuple is created, its elements cannot be changed, added, or removed.
List: Mutable, meaning you can modify a list by adding, removing, or changing its elements.

my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This will raise a TypeError

my_list = [1, 2, 3]
my_list[0] = 10  # This is allowed
Syntax:

Tuple: Defined using parentheses ().
List: Defined using square brackets [].

my_tuple = (1, 2, 3)
my_list = [1, 2, 3]
Performance:

Tuple: Generally faster than lists for iteration and access because of their immutability.
List: Slightly slower due to the overhead of allowing modifications.
Use Cases:

Tuple: Often used for fixed collections of items, such as coordinates (x, y), or when you want to ensure that the data cannot be modified.
List: Used for collections of items that may need to be changed, such as a list of user inputs or a collection of items that can grow or shrink.
Methods:

Tuple: Has fewer built-in methods (e.g., count(), index()) because they are immutable.
List: Has a wider range of methods (e.g., append(), remove(), extend(), sort(), etc.) that allow for more flexible manipulation.
Memory Consumption:

Tuple: Generally consumes less memory than lists due to their immutability.
List: Consumes more memory because of the overhead associated with dynamic resizing and mutability.
Summary
In summary, tuples are immutable, ordered collections defined with parentheses, while lists are mutable, ordered collections defined with square brackets. The choice between using a tuple or a list depends on the specific requirements of your program, such as whether you need to modify the collection or ensure its integrity.

"""



