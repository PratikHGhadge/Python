# Exeercise , Number guessing game
# make a variable , like winning_number to
# ask user to guess a number .
# if user guees corectly then print "you win!!!"
# if user didn't guessed lower than actual number then print "too low "
#     if user gueesed higher than actual number then print "too heigh"
#
# google "how to generat random number in python " to generat random
# winning number

wining_number = int(input("guees a number between 1 to 20"))
if wining_number == 11 :
    print("you gussed right you Win!!!!")
else:
    if wining_number>11:                     # nasted if else
        print("number is too high ")
    else:
        wining_number<11
        print("number is too low")
