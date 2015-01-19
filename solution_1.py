# solution_1.py
#     A program to calculate Fibonacci sequence


def main():
    
    number = eval(input("Please input a number: "))
    sequence = [1, 1]
    for item in range(2, number):
        sequence.append(sequence[item - 1] + sequence[item - 2])

    #print(sequence)
    print()        
    print("The Fibonacci number is", sequence[number - 1])


main()
