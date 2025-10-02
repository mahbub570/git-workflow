class SexyComplement:
    def __init__(self, number, base):
        self.number = number
        self.base = base
        self.digits = len(str(number))
    
    # r-1's complement
    def r_minus_1(self):
        return int(''.join(str(self.base-1 - int(d)) for d in str(self.number)))
    
    # r's complement
    def r(self):
        return self.base ** self.digits - self.number
    
    # pretty print
    def show(self):
        print(f"\nNumber: {self.number} | Base: {self.base} | Digits: {self.digits}")
        print(f"(r-1)'s complement: {self.r_minus_1()}")
        print(f"r's complement: {self.r()}\n")


# -----------------------------
# Run the sexy code
# -----------------------------
if __name__ == "__main__":
    n = int(input("Enter the number: "))
    b = int(input("Enter the base (e.g., 10, 13, 2): "))
    SexyComplement(n, b).show()
