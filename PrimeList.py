def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

original_list = eval(input("Enter the elements:"))

prime_numbers_list = [num for num in original_list if is_prime(num)]
print(f"The list of prime numbers is: {prime_numbers_list}")
