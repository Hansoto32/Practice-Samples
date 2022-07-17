###DICTIONARIES###
### YOU USE THIS TO STORE KEY VALUE PAIRS ###

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Jan"])
print(monthConversions.get("Mar"))
print(monthConversions.get("Lem", "Not a Valid Key"))


### WHILE LOOPS ###
i = 1
while i <= 10:
    print(i)
    i += 1   ## THIS IS SHORTHAND FOR I = I + 1

print("Done with Loop")


### FOR LOOPS ###
friends = ["Aldo", "Sam", "Mike"]

for index in range(3):
    print(friends[index])
    if index == 0:
        print("First iteration.")
    else:
        print("Not 1st iteration.")

## YOU CAN ALSO MAKE EXPONENT FUNCTIONS USING FOR LOOPS ##

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(4, 5))

##2D Lists##

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:
    for col in row:
        print(col)

#######WORKING WITH FILES##########

games_list = open("Games.txt", "r")
games_list.readable()
games_list.close()