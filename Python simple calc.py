

message_choose_operation = """
    Choose your operation

    [1] Addition
    [2] Subtraction
    [3] Multiplication
    [4] Division
    [5] Exponentiation
    [6] Exit

    Choice: """

def calculator(): 
    

    result = 0

    choice = input(message_choose_operation)

    if choice == "1":
        print ('\tTell me two numbers')
        X = input("\tAddend 1: ")
        Y = input("\tAddend 2: ")
        result = int(X) + int(Y)
        print ("\tSum: " + str(result))

    elif choice == "2":
        print ('\tTell me two numbers')
        X = input("\tMinuend: ")
        Y = input("\tSubtrahend: ")
        result = int(X) - int(Y)
        print ("\tDifference: " + str(result))

    elif choice == "3":
        print ('\tTell me two numbers')
        X = input("\tFactor 1: ")
        Y = input("\tFactor 2: ")
        result = int(X) * int(Y)
        print ("\tProduct: " + str(result))

    elif choice == "4":
        print ('\tTell me two numbers')
        X = input("\tDividend: ")
        Y = input("\tDivisor: ")
        result = int(X) / int(Y)
        print ("\tThe remainder is:" + str(result))

    elif choice == "5":
        print ('\tTell me two numbers')
        X = input("\tBase: ")
        Y = input("\tExponent: ")
        result = int(X) ** int(Y)
        print ("\tThe exponential result is: " + str(result))
    elif choice == "6":
        exit()
    else:
        print('\tPlease enter a valid Operation')

#_start
while True:    
    calculator()
