#!/usr/bin/env python3
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.
calc1 = '0.0'
calc2 = '0.0'
operation = ""
while calc1 != "q":
#    print("\nWhat is the first operator? Or, enter q to quit: ")
    #calc1 = raw_input("\nWhat is the first operator? Or, enter q to quit: ")
    calc1 = input("\nWhat is the first operator? Or, enter q to quit: ")
    print('calc1')
    if calc1 == "Q":
        break
    calc1 = float('calc1')
#    print("\nWhat is the second operator? Or, enter q to quit: ")
    #calc2 = raw_input("\nWhat is the second operator? Or, enter q to quit: ")
    calc2 = input("\nWhat is the second operator? Or, enter q to quit: ")
    print('calc2')
    if calc2 == "q":
        break
    calc2 = float('calc2')
#    print("Enter an operation to perform on the two operators (+ or -): ")
    #operation = raw_input("Enter an operation to perform on the two operators (+ or -): ")
    operation = input("Enter an operation to perform on the two operators (+ or -): ")
    print('operation')
    if operation == "+":
        #print("\n" + str(calc1) + "+" + str(calc2) + "=" + str(calc1 + calc2))
        print("\n" + int('calc1') + "+" + int('calc2') + "=" + int('calc1' + 'calc2'))
    if operation == "-":
        #print("\n" + str(calc1) + "-" + str(calc2) + "=" + str(calc1 - calc2))
        print("\n" + int('calc1') + "-" + int('calc2') + "=" + int('calc1' - 'calc2'))
    else:
        print("\n Not a valid entry. Restarting...")

