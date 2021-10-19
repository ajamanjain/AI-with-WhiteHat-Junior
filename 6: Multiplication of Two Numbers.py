# Write your code to multiply two numbers

# Step 1: Ask the user to enter the first number as an integer and then store it in a variable 'num_1'.
num_1 = int(input("Enter the first number as an Interger : "))

# Step 2: Ask the user to enter the second number as an integer and then store it in a variable 'num_2'.
num_2 = int(input("Enter the second number as an Interger : "))

# Step 3: Create a function and name it 'multiplier()' which takes two inputs, 'num1' and 'num2'.
def multiplier(num1,num2):

# Step 4: Multiply the input parameters using the '*' operator and store the result in a variable.
  result = num1 * num2
  
# Step 5: Print the result in the output using the 'return' keyword. 
  return result

# Step 6: Call the 'multiplier()' function and pass the variables 'num_1' and 'num_2' as an input.
multiplier(num_1,num_2)
