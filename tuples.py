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
tup3 = ("hello",) # single value in tuple 
tup4 = (55.0,)
print(type(tup2), type(tup3), type(tup4))
print(tup2,tup3,tup4)
# we should write single element by using the(,) after the element, otherwise it does not take that value as the tuple.
# for example:
for_eg = (1)
for_eg1 = ("hello")
for_eg2 = (66.0)
print(type(for_eg),type(for_eg1),type(for_eg2))
print(for_eg,for_eg1,for_eg2)
# in this given example it does not take as tuple instead of this will take as the int(),str(),float() because the singlr element doesn't ends with the (,)


