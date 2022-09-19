# List can contain heterogenious data, that is, data of different types.
# For example, the list contains student first name (string), 
# last name(string), 
# grade point average (a float),
# graduation year(int)
student_info = ['Ramesh', 'Sundar', 8.31, 2022 ]

# You refer a list element by writing the list's name followed by the element index.
# that is it's postiion number enclosed in square brackets ([])
# In the example above to access the first element, use the index 0.
print(student_info[0])
# Similarly to access the second element the index will be 1
print(student_info[1])
# Dtermining the list length
student_info_len = len(student_info)
print('The length of the list "student_info" is:', end='')
print(student_info_len)
# Accessing elements from the end of the list with Negetive Indices
# List can also be accessed from the end by using negetive indices
last_element = student_info[-1]
print(f'The last element is {last_element}. This element was accessed using the index -1')
# The first element can be accessed using -4
first_element = student_info[-4]
print(f'The first element is {first_element}. This element was accessed using the index -4')
# List are mutable - their elements can be modified
student_info[-1]=2021
print(student_info)
# Some sequences are immutable - They cannot be modified
greetings = 'Namaste'
print(greetings[2])
# geetings[2] = 'M' # Uncomment this line when you want to see that strings are not mutable

# Passing Lists to functions
# All objects are passed by reference to a function
def modify_elements(items):
	"""Multiplies all elements in items by 2."""
	for i in  range(len(items)):
		items[i] *= 2
	return items
# define the number list		
numbers = [2, 6, 10, 20, 50, 88, 120]
print(f'The modified elements are {modify_elements(numbers)}')
# Passing a tuple to the modify_elements function
# When you pass a tuple to a function, attempting to modify the tuple's immutable elements
# result in a type error
numbers_tuple = (10, 20, 30)
# The error is a TypeError. 'tuple' object does not support item assignment
#print(f'The modified tuples are {modify_elements(numbers_tuple)}')

# Sorting Lists
# A common computing task called sorting enables you to arrange data in either ascending
# or descending order.
# List method "sort" modifies a list to arrange it's elements in ascending order.
# List modifies a list to arrange it's elements in ascending order.
numbers = [10, 3, 7, 1, 8, 19, 11, 6]
numbers.sort()
print(f'the sorted list is {numbers}')
# Sorting a List in Descending Order
# Sorting a List in Descending Order
# To sort a list in descending order, call list method sort with the optional
# keyword argument reverse set to True( False is set by default)
numbers.sort(reverse=True)
print(f'The list sorted in descending order is {numbers}')
#Sorted
# The build in function sorted returns a new list containing the sorted
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
sorted_numbers = sorted(numbers)
print(f'The sorted number is {sorted_numbers}')
# Few more examples
letters = 'fadgchjebi'
print(f'The sorted leters is {sorted(letters)}')
colors = ('red', 'orange', 'yellow', 'green', 'blue')
print(f'The sorted colors is {sorted(colors)}')
foods = ['Cookies', 'pizza', 'Grapes','apples', 'steak', 'Bacon']
print(f'Food items sorted by foods {sorted(foods)}')

# List Methods
color_names = ['orange', 'yellow', 'green']
color_names.insert(0, 'red')
print(color_names)
# Adding an element to the end of the list
color_names.append('blue')
print(color_names)
# Adding all the elements of a sequence to the end of the list
color_names.extend(['indigo', 'violet'])
print(color_names)
# Removing the first occurrence of an element in a List
color_names.remove('green')
print(color_names)
# clear all the elements of a list
color_names.clear()
print(color_names)
print(color_names[:])
# Count the number of response of an element. 
responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 2]
for i in range(1, 6):
	print(f'The number of count of {i} is {responses.count(i)}')
# Searching Sequences
# Often, you'll  want to determine whether a sequence(such as a list, tuple or string)
# contains a  value that matches a particular key value.
# Searching is the process of locating a key.

# List Method Index
# List method index takes an argument a search key-- The value to locate in the list
# Then searches through the list from index 0 and returns the index of the first element
# That matches the key
numbers = [3, 7, 1, 4, 2, 8, 5, 6]
position = numbers.index(5)
print(f'Position of key 6 is {position}')
# if the key does not exists the ValueError is thrown
# The error message is ValueError:100 is not in list
# position = numbers.index(100) # Uncommenting this line will thrown a ValueError
# Operator in and not in.
print(f'Does 1000 exists in numbers list {1000 in numbers}')
print(f'Does number 5 exists in numbers list {5 in numbers}')
# Using operator in to Prevent a ValueError
# You can use the operator in to ensure that calls to method index does not result in
# ValueError for search keys that are not in the corresponding sequence
key = 1000
if key in numbers:
	print(f'Found {key} at index {numbers.index(key)}')
else:
	print(f'{key} not found in list numbers')
# Example of in and index
# Create a five element list containing 67, 12, 46, 43, 13
# Then use list method index to search for a 43 and 44. Ensure a no value error occurs
# When searching for 44.

numbers = [67, 12, 46, 43, 13]
numbers_search = [43, 44]
for number in numbers_search:
	if number in numbers:
		print(f'{number} is in list {numbers}')
	else:
		print(f'{number} is not in the list')
		
# Other List methods
# List also have methods to add and remove elements
color_names = ['red', 'orange', 'yellow', 'green', 'blue']
# Inserting an element at a specific list index
# Method insert adds a new item at a specified index. The following inserts 'red' at index 0
color_names.insert(0, 'red')
# Method Insert adds a new item at a specified index. The following inserts 'lilac' at index 2
color_names.insert(2, 'lilac')
print(f'The color list after 2 insert operations is {color_names}')
# adding an element at the end of the list
# You can add an element to the end of the list using the method append
# You can add an element to the end of yje list using the method append
color_names.append('white')
print(f'The color list after color white was added to the end of the lis(append){color_names}')
# Adding all the elements of a sequence to the End of the list
color_names.extend(['indigo', 'violet'])
print(color_names)
color_names.extend(['pink', 'grey'])
print(color_names)
# This is equivalent to the +=
sample_list = []
sample_list.extend('abc')
print(sample_list)
sample_list = []
sample_list += 'abc'
print(sample_list)
t = (1, 2, 3)
sample_list.extend(t)
# Rather than creating a temporary variable like t, to store the tuple, before
# appending it to a list, you may want to pass a tuple directly to extend. In this case
# The tuple parenthesis is required, because extend expects one iterable argument.
sample_list = []
sample_list.extend('abc')
sample_list.extend((1,2,3,))
print(sample_list)
# removing the first occurrence of an element from a list
color_names.remove('green')
print(f' color list after removing green = {color_names}')
# Emptying the list
# To delete all the elements of a list use the clear method
color_names.clear()
print(f'After clearing the color list :{color_names}')
color_names.reverse()
print(f'The reverse of list is {color_names}')

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
def is_odd(x):
	"""Returns True if x is odd"""
	return x%2 != 0
	
print(list(filter(is_odd, numbers)))

marks = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65, 44, 78, 21, 30, 66, 88]

def is_distinction_student(x):
	"""checks if marks > 70 then return True"""
	return x > 75
		
distinction_marks = list(filter(is_distinction_student, marks))
print(f'The distinction marks {sorted(distinction_marks, reverse=True)}')

# List Comprehensions
# List comprehensions can replace many for statements that iterate over existing sequences
# and create new list
list_numbers = []
for i in range(1, 6):
	list_numbers.append(i)
print(list_numbers)
# Using list comprehensions to create a list of integers
# Using list comprehensions to create a list of integers
# we can accomplish the same task using a single line of code with a list comprehensions
list_numbers = [item for item in range(1, 6)]
print(list_numbers)
# The list's comprehension for clause
# for item in range(1, 6), iterates over the sequence produced by range(1, 6)
# For each item, the list comprehension evaluates the expression to the left of the
# for clause and place the expression's value in the new list

# In the above example, the list's comprehension for clause will iterate over the range(1,6)
# For each item, the list comprehension evaluates the expression to the left of the
# for the for clause,(In the scenario, the item itself) and places the expression's value
# in the new list

# Mapping: Performing Operations in a List Comprehension's Expression
# A list comprehension expression's can perform different tasks, such as calculation
# that map elements to new values possibly of differnt types.
# Mapping is a common functional style programming operation that produces a result
# with the same number of elements as the original data being mapped.
# The following list comprehension, maps every element to its cube.
number_cubes = [item ** 3 for item in range(1, 6)]
print(f'The cube of the list is {number_cubes}')
# Filtering: List comprehension with if clause
list4 = [item for item in range(1, 11) if item % 2 == 0]
list4 = [item for item in range(1, 11) if item%2 == 0]
print(list4)
# list comprehension that processes another list items
colors = ['red', 'orange', 'yellow', 'green', 'blue']
new_color = [item.upper().strip() for item in colors]
print(new_color)
# find the elements which are boolean elements in a list
mix_list = ['Purnendu', 0, 1, True, 199, False]
bool_list = [item for item in mix_list if 'bool' in str(type(item))]
print(bool_list)
# Use a list comprehension to create a list of tuples containing the numbers 1-5 and
# Their cubes - that is [(1, 1), (2, 8), (3, 27), ...]
cubes = [(item, item ** 3) for item in range(1, 6)]
print(cubes)
# Use a list comprehension and the range function with a step to create 
# a list of the multiples of 3 that are less than 30.
multiples_of_three = [item for item in list(range(3,31,3))]
# The preceding section introduced functional style features, like list comprehension.
# Now we will demonstrate the built-in filter and map function for filtering and mapping
# respectively

# Filtering a Sequence value with built in filter function
numbers = [10, 4, 6, 7, 3, 89, 65, 77, 86, 54,  3, 1, 5, 88]
def is_odd(x):
	"""Returns true only if x is odd"""
	return x%2==1
odd_numbers = list(filter(is_odd, numbers))
print(f'The odd elements from the numbers list is {odd_numbers}')
# functions that receive other functions as arguments are a functional-style capability
# called higher order functions. For example, filter first argument must be a function
# that receives one argument and returns True if the value should be included in the result
# The function is_odd return's True if the number is an odd number
# The filter function calls the function once for each element of the second argument
# which is an iterable(numbers variable in the case above)
# filter returns an iterator, so filter results are not 
# produced until you iterate through them. This is an example of Lazy evaluation
# we can obtain the same result from the below code
odd_numbers = [item for item in numbers if  item%2 == 1]
print(f'The odd numbers are {odd_numbers}')
# Using a lamdba rather than a function
# For simple functions like is_odd that returns only a single expression value,
# you can use a lambda function(or simply a lambda) to define the function inline where it is needed
odd_numbers = list(filter(lambda x: x%2 != 0, numbers))
print(f'odd numbers using the Lambda expression {odd_numbers}')
# A lambda expression is an anonymous function that is a function without a name
# find the boolean elements in a heterogeneous list
random_list = ['Purnendu', 89, 88, True, 7292.2222, 'Mukherjee', 87, False]
boolean_list = list(filter(lambda x : 'bool' in str(type(x)), random_list))
print(f'The boolean value from the list are {boolean_list}')
# Map a sequence value to a new value
# Let's use the Builtin function map with the lambda to square each value in numbers
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f'The squared numbers are {squared_numbers}')
# Function map's first argument is a function that receives one value and 
# returns a new value--In this case a lambda that squares its argument.
# The second argument is an iterable of values to map. Function map uses lazy evaluation
# so we pass it to the list function to get the iterator that map returns
# Here's an equivalent list comprehension
[item ** 2 for item in numbers]
#Using filter and map together
odd_number_sqaured = list(map(lambda x: x** 2, filter(lambda x : x%2 !=0, numbers)))
