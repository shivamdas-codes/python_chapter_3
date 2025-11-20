# eg: 1
tup = (3,4,5,6,8) #tuple values
print(type(tup))  #type of tuple
print(tup[0])
print(tup[1])
print(tup)
# tup[2] = 10    this represents assign or replace a new value with the old value, which is not valid in the tuples and immideatly it returns error.


# eg: 2
tup1 = () #an empty tuple
print(type(tup1))
print(tup1)
# this is absolutly valid in the tuples, we can assign the empty value in the tuples


# eg: 3
tup2 = (1,)  # single valuie in tuple
tup3 = ("hello",) # single value in tuple should be represented in (,)
print(type(tup2), type(tup3))
print(tup2,tup3)
# we should write single element by using the(,) after the element, otherwise it does not take that value as the tuple.