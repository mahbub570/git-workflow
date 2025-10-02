class ComplementCalculator:
    def __init__(self, number: int, base: int):
        self.number = number
        self.base = base
        self.digits = len(str(number))
    
    def r_minus_1_complement(self):
        """
        (r-1)'s complement: Replace each digit d with (base-1 - d)
        """
        num_str = str(self.number)
        complement_digits = [(self.base - 1) - int(d) for d in num_str]
        complement_str = ''.join(str(d) for d in complement_digits)
        return int(complement_str)
    
    def r_complement(self):
        """
        r's complement = (r^n - number)
        """
        power = self.base ** self.digits
        return power - self.number

    def show_steps(self):
        print(f"\nNumber: {self.number}, Base: {self.base}, Digits: {self.digits}")
        print(f"Step 1: r^n = {self.base}^{self.digits} = {self.base ** self.digits}")
        print(f"Step 2: r's complement = r^n - number = {self.base ** self.digits} - {self.number}")
        print(f"Result: {self.r_complement()}\n")


# -------------------------------
# Interactive part
# -------------------------------
if __name__ == "__main__":
    number = int(input("Enter the number: "))
    base = int(input("Enter the base (e.g., 10 for 10's, 13 for 13's, 2 for binary): "))

    calc = ComplementCalculator(number, base)

    choice = input("Do you want (r-1)'s complement or r's complement? (type r-1 / r): ").strip()

    if choice == "r-1":
        result = calc.r_minus_1_complement()
        print(f"\n({base}-1)'s complement of {number} = {result}")
    else:
        calc.show_steps()
