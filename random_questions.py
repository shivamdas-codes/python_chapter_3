# # (1).INFINITE LOOP EXAMPLE:
# temp = 0
# while temp <100:    # less than 100
#     temp += 1       # increment by 1
#     if temp == 100:
#         temp = 0
# # this is basically an infinite loop which never ends because when temp reaches 100 it is again assigned to 0.


# # (2).EXPONENTIATION OPERATOR:
# a = 2**3    # 2 raised to the power 3
# b = a**2    # a raised to the power 2
# print(b)
# c = 2**3**2 # 2 raised to the power (3 raised to the power 2)
# print(c)


# # (3).BOOLEAN ARITHMETIC:
# x = [True,True,(True+1)*4]  #true =1
# y = False*3 + 1 #false=0
# for i in range(y+sum(x)-9):
#     print(sum(x)+i)


# # (4).STRING SLICING:
# s = "butterfly" # index started from 0 to 8
# s = s[2:]   # index sliced from 2 to end
# # now this become "tterfly"
# s = s[:5] + s[-2]
# # now take the first 5 char and last 2 char (this become "tterf" + "l" = "tterfl")
# print(s)


# # (5).FIND METHOD AND STRING SLICING:
# string = "python"
# print(string[string.find('t') + 3:])  # find the index of 't' and slice from that index +3 to end


# (6).