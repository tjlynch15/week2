# solution_5.py
#     A program to determine prime number

import math

def primeNum():
    
    number = eval(input("Please enter a positive whole number greater than 2: "))

    prime = True
    for integer in range(2, int(math.sqrt(number)) + 1):
        if number%integer == 0:
            prime = False
            break

    if number <= 2 or number - int(number) != 0:
        print("Invalid entry")

    elif number > 2 and prime == True:
        print("Prime number")

    else:
        print("Not a prime number")

        
def main():

    primeNum()
    print()
    answer = input("Do you want to enter another number? (y or n): ")
    while answer == "y":
        print()
        primeNum()
        print()
        answer = input("Do you want to enter another number? (y or n): ")                        

main()
