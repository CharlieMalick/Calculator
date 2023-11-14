while True:
    start = input("Welcome to the calculator! Do you want to add[1], subtract[2], multiply[3], divide[4], raise to a power [5], find a square root[6], find a modulus[7], or exit[8]?\n")

    karissa = int(start)

    if(karissa == 8):
        print("Thank you for using the calculator, have a good day!")
        break

    if(karissa == 1):
        print("Looks like you want to add!")
        first_number_add = float(input("Give me your first number:\n"))
        second_number_add = float(input("Give me your second number\n"))
        addition = first_number_add + second_number_add
        print("The sum of your numbers is " + str(addition) + ".")
    elif(karissa == 2):
        print("Looks like you want to subtract!")
        first_number_subtract = float(input("Give me your first number:\n"))
        second_number_subtract = float(input("Give me your second number\n"))
        subtraction = first_number_subtract - second_number_subtract
        print("The difference of your numbers is " + str(subtraction) + ".")
    elif(karissa == 3):
        print("Looks like you want to multiply!")
        first_number_multiply = float(input("Give me your first number:\n"))
        second_number_multiply = float(input("Give me your second number\n"))
        multiplication = first_number_multiply * second_number_multiply
        print("The product of your numbers is " + str(multiplication) + ".")
    elif(karissa == 4):
        print("Looks like you want to divide!")
        first_number_divide = float(input("Give me your first number:\n"))
        second_number_divide = float(input("Give me your second number\n"))
        if(second_number_divide == 0):
            print("You cannot divide by zero, that is invalid.")
            continue
        else:
            division = float(first_number_divide)/float(second_number_divide)
            print("The quotient of your numbers is " + str(division) + ".")
    elif(karissa == 5):
        print("Looks like you want to work with exponents!")
        first_number_exponent = float(input("Give me your first number:\n"))
        second_number_exponent = float(input("Give me your second number\n"))
        exponent = first_number_exponent ** second_number_exponent
        print("Your number " + str(first_number_exponent) + " raised to the power of " + str(second_number_exponent) + " is " + str(exponent))
    elif(karissa == 6):
        print("Looks like you want to find a square root!")
        root_input = float(input("Give me your number:\n"))
        root = root_input ** 0.5
        print("The square root of your number is " + str(root))
    elif(karissa == 7):
        print("Looks like you want to find a modulus!")
        modulo_one = float(input("Give me your first number:\n"))
        modulo_two = float(input("Give me your second number:\n"))
        modulus = modulo_one % modulo_two
        print("The modulus of " + str(modulo_one) + " and " + str(modulo_two) + " is " + str(modulus))
    else:
        print("Invalid input, please try again.")

#things to add: 
#exponent, modulus, square root functions
#error handling
#trig functions, log (math module)