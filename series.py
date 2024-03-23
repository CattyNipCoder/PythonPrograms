import math

def calculate_series_sum(x, n):
    series_sum = 0
    term = 1  # The first term in the series

    for i in range(1, n + 1):
        term *= x / i  # Calculate the next term using the previous term
        series_sum += term

    return series_sum

# Example usage:
x_value = float(input("Enter the value of x: "))
terms_count = int(input("Enter the number of terms (n): "))

result = calculate_series_sum(x_value, terms_count)
print(f"The sum of the series is: {result}")