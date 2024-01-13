def is_prime(number):
    if number < 2:
        return None
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            return False
    return True
def find_divisors(number):
    if number < 2:
        return None
    divisors = [1] 
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            divisors.extend([i, number // i])
    return divisors + [number]
number = int(input("Enter a number here: "))
if is_prime(number):
    print(f"The number {number} is a prime number.")
else:
    divisors=find_divisors(number)
print(f"The divisors of {number} are {divisors}.")