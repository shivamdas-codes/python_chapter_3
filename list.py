# example: 1
num = [23, 45, 67, 89, 12, 90, 34, 56, 78, 11]
print(type(num))
print(len(num))
print(num[0])   # prints the first element of the list
print(num[4])   # prints the fifth element of the list
print(num)


# example: 2
student_info = ["shivam", 99.0, 10, "hyderabad" ]
print(student_info)
# we can access many values in a single list for example: str(), int() etc....


# example: 3
student = ["shivam", 99.5, 18, "hyderabad"]
print(student[3])
print(student[0],student[1])
student[3] = "USA"
print(student)
# student1 = ["shivam", 77.6, 10, "hyderabad"]
# print(student[5])
"""we can able to print any index that are present in the list and we can able to change the index according to the sitution 
if we try to print index which is not there in the list then it will show as error"""


# example: 4
marks = [56, 78, 46, 87, 86, 45]
print(marks[1:4]) 
print(marks[:5])
print(marks[1:])
# same as string slicing (positive slicing)

# example: 5
marks1 = [65, 74, 83, 67, 66, 89]
print(marks1[-3:-1])
print(marks1[:-1])
print(marks1[-4:])
# same as string slicing (negative slicing)



# METHODS IN LIST
# (1). append()
list1 = [6, 7, 8, 9, 5]
list1.append(10)
print(list1)
# this function/method in list is used to add an element to the end of the list


# (2). sort()
marks2 = [6, 7, 3, 5, 9]
marks2.sort()
print(marks2.append(10))
# if we give this method inside the print value it prints the number but it always shows the "none value"
# print(marks2.sort()) it will print the "none value"
print(marks2)
# this function/method in list is used to arrange the elements in the right order or we can say that it arrange in the ascending order
listt = ["e", "d", "a", "b", "c"]
list2 = ["mango", "banana", "apple", "grapes"]
listt.sort()
list2.sort()
print(listt)
print(list2)
# this not only applicable for the integer but also applicable to the strings as well, this mainly takes in albhabetical order


# (3). sort(reverse = True)
list = [6,4,7,8,3,2]
print(list.sort(reverse = True))
# the above line prints the NONE value
list.sort(reverse = True)
print(list)
list1 = ["e", "d", "a", "b", "c"] 
list2 = ["apple", "grapes", "banana", "mango"]
list1.sort(reverse = True)
list2.sort(reverse = True)
print(list1)
print(list2)
# the reverse() sorting prints the value in descending order


# (4). reverse()
list = [4,6,7,3,4,8]
list.reverse()
print(list)
list2 = ["apple", "mango", "grapes"]
list2.reverse()
print(list2)
# this method is used to reverse the list compltely 


# (5). insert()
list = [66, 77, 88, 44, 11]
list.insert(77, 99)
print(list)
# this method basically used to insert any kind of element in the particular index.
fruits = ["apple", "mango", "grapes"]
fruits.insert(0,"banana")
print(fruits)
# if the value is in the form of the strings then it will print error if you try to replace it with another string 
# NOTE: this method doesn't replace or delete any value to insert the new element 


# (6). remove()
numbers = [44, 77, 44, 88, 99, 22, 44]
numbers.remove(44)
print(numbers)
objects = ["car", "bottle", "books", "pen"]
objects.remove("car")
print(objects)
# this method is mainly used to remove the first occurance of the given list


# (7). pop()
num = [3, 5, 2, 6, 7, 1]
num.pop(3)  #the element which is given is an index
print(num)
# the pop() method is used to completely delete the index
var = ["apple", "mango", "grapes"]
var.pop(2)
print(var)



# this example contains all the methods that are present in the list
# insert(), remove(), append(), sort(), pop(), reverse()
n = [12]
n.insert(0,5)
n.insert(1,10)
n.insert(0,6)
print(n) 
n.remove(6)
n.append(9)
n.append(1)
n.sort()
print(n) 
n.pop()
n.reverse()
print(n) 