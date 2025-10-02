def r_complement():
    # take input from user
    number = int(input("Enter the number: "))
    base = int(input("Enter the base (e.g. 10 for 10's complement, 13 for 13's complement): "))

    # count digits
    n = len(str(number))

    # formula: base^n - number
    result = (base ** n) - number

    print(f"{base}'s complement of {number} is: {result}")


# Run
r_complement()
