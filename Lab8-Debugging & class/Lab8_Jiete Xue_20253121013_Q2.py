class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {-self.imaginary}i"
    
    def add(self, other):
        new_real = self.real + other.real
        new_imaginary = self.imaginary + other.imaginary
        return ComplexNumber(new_real, new_imaginary)

    def subtract(self, other):
        new_real = self.real - other.real
        new_imaginary = self.imaginary - other.imaginary
        return ComplexNumber(new_real, new_imaginary)
    

if __name__ == "__main__":
    # Instantiate two ComplexNumber objects
    c1 = ComplexNumber(3, 4)
    c2 = ComplexNumber(1, -2)
    # Add the two complex numbers
    result_add = c1.add(c2)
    print(result_add) # Should display "4 + 2i"
    # Subtract the second complex number from the first one
    result_subtract = c1.subtract(c2)
    print(result_subtract) # Should display "2 + 6i