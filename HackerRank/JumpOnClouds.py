c = [0, 0, 1, 0, 0, 1, 0]
i = 0
jump = 0
while(i < len(c)):
    if((i+2) < len(c) and c[(i+2)] == 0):
        jump += 1
        i += 2
    # else:
    #     i += 1
    #     jump += 1
    elif((i+1) < len(c) and c[(i+1)] == 0):
        jump += 1
        i += 1
    else:
        i += 1


print(jump)
