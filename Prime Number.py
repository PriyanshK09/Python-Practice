# Detect prime number in Python

# Function to check if a number is prime
def isPrime(n):
    # Corner case
    if n <= 1:
        return False

    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

# Driver Program
if __name__ == "__main__":
    n = 11
    if isPrime(n):
        print("Yes")
    else:
        print("No")