import random as r

print("Welcome to the Powerball!")
print("It's time to choose your five numbers ranging from 1-20.")

while True:
    number1 = input("What is your first number? ")

    try:
        number1 = int(number1)
    except ValueError:
        print("try again")
        continue
    if number1 <= 0:
        print("Number must be higher than 0")
    elif number1 < 21:
        break
    else:
        print("Did you not read? Only numbers 1-20!")


while True:
    number2 = input("What is your second number? ")

    try:
        number2 = int(number2)
    except ValueError:
        print("try again")
        continue
    if number2 == number1:
        print("Please no duplicate numbers")
    elif number2 <= 0:
        print("Number must be higher than 0")
    elif number2 < 21:
        break
    else:
        print("Did you not read? Only numbers 1-20!")

while True:
    number3 = input("What is your third number? ")

    try:
        number3 = int(number3)
    except ValueError:
        print("try again")
        continue
    if number3 == number2:
        print("Please no duplicate numbers")
    elif number3 <= 0:
        print("Number must be higher than 0")
    elif number3 == number1:
        print("Please no duplicate numbers")
    elif number3 < 21:
        break
    else:  
        print("Did you not read? Only numbers 1-20!")

while True:
    number4 = input("What is your fourth number? ")

    try:
        number4 = int(number4)
    except ValueError:
        print("try again")
        continue
    if number4 == number3:
        print("Please no duplicate numbers")
    elif number4 <= 0:
        print("Number must be higher than 0")
    elif number4 == number2:
        print("Please no duplicate numbers")
    elif number4 == number1:
        print("Please no duplicate numbers")
    elif number4 < 21:
        break
    else:
        print("Did you not read? Only numbers 1-20!")

while True:
    number5 = input("What is your fifth number? ")

    try:
        number5 = int(number5)
    except ValueError:
        print("try again")
        continue
    if number5 == number4:
        print("Please no duplicate numbers")
    elif number5 <= 0:
        print("Number must be higher than 0")
    elif number5 == number3:
        print("Please no duplicate numbers")
    elif number5 == number2:
        print("Please no duplicate numbers")
    elif number5 == number1:
        print("Please no duplicate numbers")
    elif number5 < 21:
        break
    else:
        print("Did you not read? Only numbers 1-20!")

your_numbers = [number1, number2, number3, number4, number5]
print(f"So here are the numbers you chose: {your_numbers}")

def Powerball():
    result = []
    for i in range(5):
        number = r.randint(1,20)
        while (number in result):
            number = r.randint(1,20)
        result.append(number)
    result.sort()
    return result

if __name__ == '__main__':
    result = Powerball()
    print("The Powerball numbers are:")
    print (result)

number_of_correct = len(list(filter(lambda n: n in (your_numbers), result)))
print(f"You got {number_of_correct} out of 5 correct!")

amount_of_money_won = 0
if number_of_correct < 5:
    amount_of_money_won += number_of_correct * 1000
    print(f"You win ${amount_of_money_won}!")
elif number_of_correct == 0:
    print("You LOSE!")
else:
    if your_numbers == result:
        print("You have won the JACKPOT of $1,000,000,000")