# 1. Create a greeting for your program.
# 2. Ask the user for the city that they grew up in.
# 3. Ask the user for the name of a pet.
# 4. Combine the name of their city and pet and show them their band name.
# 5. Make sure the input cursor shows on a new line

# The solution

print("Welcome to this Band Name Generator")

City = input("In which city did you grow up?\n")

Pet = input("What is the name of your pet?\n")

Band_name = City + Pet

print("Your Band Name is: " + Band_name)
