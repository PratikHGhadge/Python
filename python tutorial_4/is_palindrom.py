# define is_palindrome function that takes one word in string as input
# and return true if it is palindrome else return false

# palindrome - word that reads same backwords as forwords

# example
# is_palindrome("madam")__________> true
# is_palindrome("naman")__________> true

#logic (algorithum)
#step 1 revers the string
#step 2 compare reversed string with original string

#Ans

def is_palindrom(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False

print(is_palindrom("naman"))
print(is_palindrom("horse"))