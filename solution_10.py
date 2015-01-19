#solution_10.py
#     A program to calculate miles per gallon


def main():

    infile = open("driving_legs.txt", 'r')
    print()

    start_odom = eval(infile.readline())
    
    total_gas = 0.0
    current_odom = start_odom
    leg = 1

    for line in infile:
        odometer, gas_used = line.split()
        odometer, gas_used = eval(odometer), eval(gas_used)
        print("Miles per gallon for leg {0}: {1:0.2f}"
              .format(leg, (odometer - current_odom)/gas_used))
                    
        current_odom = odometer
        total_gas = total_gas + gas_used
        leg = leg + 1
        
    infile.close()
        
    print()
    #print("Total mileage: ", current_odom - start_odom)
    #print("Total gas used: ", total_gas)
    print("Total miles per gallon is {0:0.2f}"
          .format((current_odom - start_odom)/total_gas))


main()
