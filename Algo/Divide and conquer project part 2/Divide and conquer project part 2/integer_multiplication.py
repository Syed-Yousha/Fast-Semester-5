# Karatsuba Algorithm for Integer Multiplication

def karatsuba(x, y):
    # Base case for recursion
    if x < 10 or y < 10:
        return x * y
    
    n = max(len(str(x)), len(str(y)))
    half = n // 2

    # Split the numbers
    high1, low1 = divmod(x, 10**half)
    high2, low2 = divmod(y, 10**half)

    # Recursively calculate three products
    z0 = karatsuba(low1, low2)
    z1 = karatsuba(low1 + high1, low2 + high2)
    z2 = karatsuba(high1, high2)

    # Combine the three results
    return z2 * 10**(2*half) + (z1 - z2 - z0) * 10**half + z0

# Example usage
if __name__ == "__main__":
    x = 1234
    y = 5678
    result = karatsuba(x, y)
    print(f"The result of {x} * {y} is: {result}")
