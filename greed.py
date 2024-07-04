# LINK:
'''
https://www.codewars.com/kata/5270d0d18625160ada0000e4/solutions/python
'''

import math
#Input:
dice = [1, 1, 1, 1, 1]

#Value_Tables:
value_table_of_threes = {"1":1000, "6":600,"5": 500, "4":400,"3":300,"2":200}
value_table_of_ones = {"5":50,"1":100}


#Function:
def score(dice):
    dice_map ={}
    for i in dice:
        if i in dice_map:
            dice_map[i] =  dice_map[i] + 1
        elif i not in dice_map:
            dice_map[i] = 1
        else:
            # Error
            raise ValueError
    score = 0
    for keys in dice_map:
        if (dice_map[keys] >= 3):

            value_1 = math.floor(dice_map[keys]/3)
            score = score + (value_1 * value_table_of_threes[str(keys)])
            remainder = dice_map[keys]%3

            if (keys == 5) or (keys == 1):
                score = score +  (value_table_of_ones[str(keys)] * remainder)


        elif (dice_map[keys] < 3) and ((keys == 5) or (keys == 1)):
            score = score +  (value_table_of_ones[str(keys)] * dice_map[keys])


    return score

# Run
print(score(dice))
