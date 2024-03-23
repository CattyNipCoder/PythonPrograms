# Get a list of numbers from the user
user_input = input("Enter a list of numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]

# Count the occurrences of the digit '2' in the list
count_of_twos = sum(str(number).count('2') for number in numbers)

# Print the result
print("Count of 2's in the list:", count_of_twos)
