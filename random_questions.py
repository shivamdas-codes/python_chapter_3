temp = 0
while temp <100:    # less than 100
    temp += 1       # increment by 1
    if temp == 100:
        temp = 0
# this is basically an infinite loop which never ends because when temp reaches 100 it is again assigned to 0.