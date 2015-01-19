# solution_4.py
#     A program to calculate Syracuse sequence


def main():
    
    nat_num = eval(input("Please input a natural number: "))
    sequence = [nat_num]

    while nat_num != 1:
        
        if nat_num%2 == 0:
            nat_num = nat_num//2
            sequence.append(nat_num)
            
        elif nat_num%2 != 0:
            nat_num = 3*nat_num + 1
            sequence.append(nat_num)
            
    print()
    print("The Syracuse sequence is:" )
    print(sequence)
    print()


main()
