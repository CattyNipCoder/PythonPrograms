def abbreviate_name(full_name):
    name_parts = full_name.split()
    
    # Extract the first letter of each part and join with a period
    abbreviated_name = '. '.join(part[0] for part in name_parts)
    
    return abbreviated_name

# Example usage:
full_name = input("Enter the full name: ")
abbreviation = abbreviate_name(full_name)
print(f"The abbreviated name is: {abbreviation}")
