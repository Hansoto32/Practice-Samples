#####LISTS#####
lucky_numbers = [12,45,10,15,2,18,9,5]
friends = ["Aldo", "Craig", "Sam", "Scott", "Dave", "Zack"] ##Brackets can store information in a list for Python to use later.
#           0       1       2       3        4      5   -1
print(friends[0]) #THIS WILL PRINT THE INDEX OF WHAT YOU PLACE INSIDE THE BRACKETS
print(friends[1:3]) #THIS WILL PRINT EVERYTHING AFTER THE INDEX IF YOU INCLUDE A NUMBER AFTER THE COLON IT WILL GRAB UP
#TO THAT INDEX POSITION

##PYTHON CAN ALSO USE CERTAIN FUNCTIONS WITH LISTS.
friends.extend(lucky_numbers) #THIS FUNCTION WILL ADD TO THE LIST YOU'RE EXTENDING TO.
friends.append("Banjo") #THIS WILL ADD WHAT YOU HAVE IN HERE TO ADD TO THE END OF THE LIST.
friends.insert(1, "Kevin") #THE FIRST VALUE IS THE INDEX OF WHERE YOU WANT TO INSERT THE 2ND VALUE.
friends.remove("Sam") #THIS CAN REMOVE SOMETHING FOR YOUR LIST.
friends.index("Kevin") #THIS SHOWS WHERE YOUR
print(friends)


####TUPLE####
#SIMILAR TO A LIST, WHERE YOU CAN STORE INFORMATION. TOUPLES ARE IMMUTABLE, MEANING THEY CANNOT BE MODIFIED OR CHANGED.
#YOU CAN ALSO CREATE A LIST OF TUPLES BY PLACING THEM IN A BRACKET.
coordinates = [(4, 5), (6, 8), (1, 4)]
print(coordinates[1])



#####FUNCTIONS#####
#YOU CAN CREATE FUNCTIONS BY USING DEF. WHEN DOING SO YOU'LL NEED TO INDENT TO STAY WITHIN THE FUNCTION YOU'RE MAKING.
##You can create and store your functions for later use.

def say_hi(name, age):                               #THIS IS WHAT YOU WILL TYPE IN TO CALL YOUR FUNCTION.
    print("Hello " + name + " you are " + str(age))
#THIS IS THE FUNCTION WE'VE MADE AND WILL DO EVERYTHING WE'VE PROGRAMMED WITHIN THE FUNCTION.
#CALLING THE FUNCTION IS WHAT IT LOOKS LIKE BELOW. YOU MUST PUT IN A NAME AND AGE PARAMETER.
say_hi("Mike", "26")
say_hi("Chris", "31")
#WITHIN THE PARENTHESIS IS THE PARAMETER NEEDED TO CALL THE FUNCTION WE'VE MADE. YOU CANNOT CALL THIS FUNCTION
#WITHOUT THE SPECIFIED PARAMETERS PLACED INSIDE THE PARENTHESIS
#YOU CAN ADD MULTIPLE PARAMETERS AND STORE THEM THE SAME WAY A VAIRABLE DOES.

def cube(num):
    return num*num*num              #THE RETURN COMMAND WILL ALLOW US TO SHOW THE VALUE OF THE EQUATION WHEN CALLING
                                    #THIS FUNCTION. WHEN IT SEE THE RETURN KEYWORD YOU CANNOT WRITE ANOTHER LINE OF
                                    #CODE UNDER IT.
print(cube(5))



#########IF STATEMENTS USING BOOLEON VALUES###########
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are male and tall.")
elif is_male and not(is_tall):
    print("You are male, but not tall.")
elif not(is_male) and is_tall:
    print("You are tall, but not male.")
else:
    print("You are either not male, or not tall.")

####USING COMPARISONS WITH IF STATEMENTS####
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print (max_num(300000, 5000, 100))


def min_num(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <= num3:
        return num2
    else:
        return num3

print (min_num(300000, 5000, 100))