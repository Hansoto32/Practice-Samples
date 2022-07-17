#This just prints the following text inside the quotes
print("Hello world!")

#Below is an example of variables and how to use them in strings.
myname = "Chris"
myage = "31"
print("Hello my name is " + myname)   ##THIS IS AN EXAMPLE OF CONCATINATION TO CONNECT THE STRINGS##
print("I am " + myage + " years old.")

###Some thing you can do with strings###
#The N after the backslash shows everything after it on the next line.
print("Giraffe\nAcademy")
#The backslash also allows you to use ",[,{,(, and other characters, within a string.
print("Giraffe\"Academy")
#The backslash alone will just print a backslash.
print("Giraffe\Academy")



##FUNCTIONS##
phrase = "Giraffe Academy"
#The first function in the example below is converting the phrase to lower case, and then asking Python if it is true or
#not.
print(phrase.lower().islower())
#The function below is showing the length of the string.
print(len(phrase))
#In Python, the 1st character in a string is position 0; so this will print a 0.
print(phrase[0])
#The index function will print the number associated with the position of the character you're trying to index.
#if the character cannot be found using the index function python will error when running the script.
print(phrase.index("G"))
#This function will replace the word Giraffe, with Elephant in the specified string.
print(phrase.replace("Giraffe", "Elephant"))
#The function below shows the absolute value of a number.
print(abs(-6))
#The power function works with the 1st number as your base and the 2nd as your power.
print(pow(5,3))
#The Max function will give us the larger of the numbers given; Min will do the opposite.
print(max(5, 8, 9))
print(min(5, 8, 9))
#The round function will round a decimal. It follows the standard rules for rounding.
print(round(8.2))

##PYTHON NEEDS TO IMPORT MODULES TO USE OTHER FUNCTIONS. (IMPORTING) THE FOLLOWING COMMAND ALLOWS YOU TO USE THESE
##EXTRA FUNCTIONS. "FROM" WILL ALLOW YOU TO GRAB THE FILE YOU NEED "MATH" WHICH YOU CAN THEN GIVE THE IMPORT COMMAND.
from math import *
#This will give the lower number in the decimal. Ciel will round your decimal up no matter what.
print(floor(1.6))
print(ceil(1.6))
#The following will give you the square root of a number.
print(sqrt(36))



##HOW TO USE NUMBERS##
#You can make simple math problems, or just print numbers. No quotes are needed.
print(5)
print(5*10-10*2) #Python knows order of operations, and you can throw in parenthesis to force the equation.
print(23%4) #THE % SYMBOL IS A MODULUS. THIS GIVES US THE REMAINDER OF THE 2 NUMBERS.

##YOU CANNOT USE NUMBERS AND STRINGS IN A COMMAND TOGETHER WITHOUT FIRST CONVERTING A NUMBER INTO A STRING.
#You can convert a number to work with a string by using the str command in front of your number.
#Then use Concatination to finish the rest of the string you want to print.
print(str(2) + " is my favorite number.")

##Numbers can also be stored into variables; They can also be converting to be used with strings.
My_num = 150
print(My_num)
print(str(My_num) + " is not my favorite number.")

###GETTING USER INPUT###
#The following command will ask the user for the prompt placed inside. You can also store it into a variable.
#you can then take the information stored into those variables for the future.
name = input("Enter your name: ")
print("It's very nice to meet you " + name)
age = input("What is your age?:")
print("Wow, " + age + " isn't even that old!")


#####BASIC CALCULATOR USING INPUT COMMANDS#####
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)     #YOU'LL WANT TO USE FLOAT WITH USER INPUT SO THEY CAN USE DECIMALS.
print(result)