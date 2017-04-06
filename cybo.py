#!/usr/bin/env python

'''
To Do
- The adjacent numbers should be distinct for a trinity
- Clearer output formatting/screen printing.
'''


import time
import random as computer
import random as user

rows = [[1,5,9],[2,6,10],[3,7,11],[4,8,12]]
columns = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
diagonals = [[1,6,11],[2,7,12]]

def checkAlignment(a,b) :
    for row in rows :
        if a in row and b in row :
            return True

    for column in columns :
        if a in column and b in column :
            return True

    for diagonal in diagonals :
        if a in diagonal and b in diagonal :
            return True

    return False

def checkTrinityColumn(nums) :
    if len(nums) != 3 :
        return False

    for column in columns :
        if nums[0] in column and nums[1] in column and nums[2] in column :
            return True

    return False

def checkTrinity(nums) :
    if len(nums) != 3 :
        return False

    for row in rows :
        if nums[0] in row and nums[1] in row and nums[2] in row :
            return True

    for column in columns :
        if nums[0] in column and nums[1] in column and nums[2] in column :
            return True

    for diagonal in diagonals :
        if nums[0] in diagonal and nums[1] in diagonal and nums[2] in diagonal :
            return True

    return False

def checkQuad(nums) :
    if len(nums) != 4 :
        return False

    for column in columns :
        if nums[0] in column and nums[1] in column and nums[2] in column and nums[3] in column :
            return True

    return False

def checkInOrder(nums) :
    if len(nums) != 3 :
        return False

    nums_reverse = nums
    nums_reverse.reverse()

    for row in rows :
        if nums == row or nums_reverse == row :
            return True

    for column in columns :
        if nums[0] in column and nums[1] in column and nums[2] in column :
            return True

    for diagonal in diagonals :
        if nums == diagonal or nums_reverse == diagonal :
            return True

    return False

def calculateScore(nums) :
    score = 0

    if len(nums) == 3 :
        if checkTrinity(nums) :
            score = 3

            if checkInOrder(nums) :
                score = 9
    elif len(nums) == 4 :
        if checkQuad(nums) :
            score = 16
        else :
            score = 3

    return score

def rollUserDice() :
    user_input = raw_input("\nPress any key to roll : ")
    user.seed(time.time())
    roll_value = user.randint(1,12)
    print "You got :",roll_value
    return roll_value

def rollComputerDice() :
    roll_value = computer.randint(1,12)
    print "Computer got :",roll_value
    return roll_value

grid = '1\t5\t9\n2\t6\t10\n3\t7\t11\n4\t8\t12'

user_data = []
computer_data = []

total_user_score = 0
total_computer_score = 0

for i in range(1,14) :
    print "\n\tRound "+str(i)+"\n"
    print grid
    user_rolls = []

    #Throw 1
    user_throw1 = rollUserDice()
    user_rolls.append(user_throw1)

    #Throw 2
    user_throw2 = rollUserDice()
    user_rolls.append(user_throw2)

    #Check if the 2nd no is in a row, column or diagnoal
    #Skip turn if not
    is_aligned = checkAlignment(user_throw1,user_throw2)
    if is_aligned :
        #Throw 3
        user_throw3 = rollUserDice()
        user_rolls.append(user_throw3)

        #Check if the user scored a trinity in a column
        is_trinity_column = checkTrinityColumn(user_rolls)

        if is_trinity_column :
            print "You got a trinity in a column:",user_throw1,user_throw2,user_throw3
            roll_again = raw_input("Do you want to roll again? (Press 'y' for yes)")
            if roll_again.startswith('y') :
                user_throw4 = rollUserDice()
                user_rolls.append(user_throw4)

    user_score = calculateScore(user_rolls)

    print "Your Score :",user_score
    user_data.append([user_rolls,user_score])

    total_user_score += user_score
    print "Your Total Score :",total_user_score


    #Computer's Turn
    print "Computer's Turn Now."

    computer_rolls = []
    #Throw 1
    computer_throw1 = rollComputerDice()
    computer_rolls.append(computer_throw1)

    #Throw 2
    computer_throw2 = rollComputerDice()
    computer_rolls.append(computer_throw2)

    #Check if the 2nd no is in a row, column or diagnoal
    #Skip turn if not
    is_aligned = checkAlignment(computer_throw1,computer_throw2)
    if is_aligned :
        #Throw 3
        computer_throw3 = rollComputerDice()
        computer_rolls.append(computer_throw3)

        #Check if the user scored a trinity (three numbers in a column)
        is_trinity_column = checkTrinityColumn(computer_rolls)

        if is_trinity_column :
            print "Computer got a trinity in a column:",computer_throw1,computer_throw2,computer_throw3
            roll_again = raw_input("Do you want computer to roll again? (Press 'y' for yes, 'r' for random)")
            if roll_again.startswith('y') :
                computer_throw4 = rollComputerDice()
                computer_rolls.append(computer_throw4)
            elif roll_again.startswith('r') :
                choice = computer.choice(['y','n'])
                if choice.startswith('y') :
                    computer_throw4 = rollComputerDice()
                    computer_rolls.append(computer_throw4)

    computer_score = calculateScore(computer_rolls)

    print "Computer Score :",computer_score
    computer_data.append([computer_rolls,computer_score])

    total_computer_score += computer_score
    print "Computer's Total Score :",total_computer_score
