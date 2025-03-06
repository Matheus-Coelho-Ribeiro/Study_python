#part one
#variables

#strongs

# first_name = "James"
# last_name = "Smith"
# food_favorite = "hot dogs"

#placeholder

# print(f"your name is {first_name} {last_name}, your favorite food is {food_favorite}")

#integer

# age = 30
# number_cell = 123456789
# quantity_food_favorite = 90

# print(f"you are {age} years old, your number cellphone is {number_cell}, you have {quantity_food_favorite} hot dogs")

#float

# pi = 3.14
# price_food_favorite = 3.75

#test

# price_all = price_food_favorite + quantity_food_favorite

# print(f"the number of pi is {pi}, one hot dog for sale by {price_food_favorite}, the all price is {price_all}")

#test is correct? yes (typecasting automaly)

#boolean

# is_online = True
# your_verification = False
# is_human = False

# if(is_online):
#     print("your are online")
# else:
#     print("your are NOT onine")

# if(your_verification):
#     print("you are permition")
# else:
    # print("you are NOT permition")

# if(is_human):
#     print("you are human")
# else:
#     print("you are robot")

#part two
#typecasting

# first_name_one = "Noah"
# number_random = 8938943
# pi = 3.141592
# is_student = True

#type()

# print(type(first_name_one))
# print(type(number_random))
# print(f"{type(pi)}")
# print(type(is_student))

# print(int(pi))
#print(int(first_name_one))# <-- error typecasting invalidation
# print(type(str(pi)))
# print(type(str(is_student)))

#part Three
#input

# name_user = input("whats your name?\n")
# print(name_user)

#exercise one rectagle area calc

leigth = float(input("whats is the leigth?"))
width = float(input("whats is the width?"))
area = leigth * width
print(f"the area totaly is {area} m²")