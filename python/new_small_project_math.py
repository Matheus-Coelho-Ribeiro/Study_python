verification = input("your was a project small in python of begginer? Y[yes] / N [not] ?")
if(verification == "Y"):
    number_one = float(input("ok, enter a number one:"))
    number_two = float(input("yes, enter a number two:"))
    number_three = float(input("finaly, enter a number three:"))
    decition = int(input("your was five options: 1 = retired as negatives numbers | 2 = retired as numbers points | 3 = get the number maximun | 4 get the number minimun | 5 = exponed first number with second number | enter a number of one was five"))
    if(decition == 1):
        print(f"number one = {abs(number_one)} | number two = {abs(number_two)} | number three {abs(number_three)}")
    if(decition == 2):
        print(f"number one = {round(number_one)} | number two = {round(number_two)} | number three = {round(number_three)}")
    if(decition == 3):
        print(f"the number maximum is {max(number_one, number_two, number_three)}")
    if(decition == 4):
        print(f"the minimum number is {min(number_one, number_two, number_three)}")
    if(decition == 5):
        print(f"{number_one} sup {number_two} is {pow(number_one, number_two)}")
else:
    print("program end")