# (1).INFINITE LOOP EXAMPLE:
temp = 0
while temp <100:    # less than 100
    temp += 1       # increment by 1
    if temp == 100:
        temp = 0
# this is basically an infinite loop which never ends because when temp reaches 100 it is again assigned to 0.


# (2).EXPONENTIATION OPERATOR:
a = 2**3    # 2 raised to the power 3
b = a**2    # a raised to the power 2
print(b)
c = 2**3**2 # 2 raised to the power (3 raised to the power 2)
print(c)


# (3).BOOLEAN ARITHMETIC:
x = [True,True,(True+1)*4]  #true =1
y = False*3 + 1 #false=0
for i in range(y+sum(x)-9):
    print(sum(x)+i)


# (4).STRING SLICING:
s = "butterfly" # index started from 0 to 8
s = s[2:]   # index sliced from 2 to end
# now this become "tterfly"
s = s[:5] + s[-2]
# now take the first 5 char and last 2 char (this become "tterf" + "l" = "tterfl")
print(s)


# (5).FIND METHOD AND STRING SLICING:
string = "python"
print(string[string.find('t') + 3:])  # find the index of 't' and slice from that index +3 to end


# (6).BOOLEAN EVALUATION:
a = "1" # non empty string
b = "0" # non empty string
# the above assign values are string type that means both a and b are "True" because non-empty strings are considered True and empty strings are considered False in boolean context.
# if any interger is assign then assume "true = 1 , false = 0"
if a and b == True:
    print("its a true statement")
else:
    print("its a false statement")


# (7).TYPE CONVERSION:
a = int("11", 2) # binary to decimal conversion
print(a)


# (8).LIST REMOVAL DURING ITERATION:
my_list = [3,4,5,6,7] #THE ELEMENTS ARE ASSIGNED FROM INDEX 0 TO 4
for i in my_list:
# THIS LOOP FOLLOWS THE ELEMENTS ONE BY ONE FROM THE LIST AND REMOVES THEM
# EXAMPLE: my_list[0], my_list[1], my_list[2]....
    my_list.remove(i)
print(my_list)


# (9).FOR LOOP WITH RANGE AND ACCUMULATION:
x = 0
for i in range(3):#the range(0,1,2) now add one after one with x
# case(1): i=0 , x=0+0=0
# case(2): i=1 , x=0+1=1
# case(3): i=2 , x=1+2=3      finally i=2 and x=3
    x += i
print(i,x)
