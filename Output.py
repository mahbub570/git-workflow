def r_complement(number: int, base: int) -> int:
    """
    Calculate the r's complement of a number.
    base = 10 means 10's complement
    base = 13 means 13's complement
    """
    # number of digits in the given number
    n = len(str(number))
    
    # r^n
    power = base ** n
    
    # complement formula: r^n - number
    return power - number

# Example usage:
print("10's complement of 15:", r_complement(15, 10))
print("13's complement of 15:", r_complement(15, 13))
