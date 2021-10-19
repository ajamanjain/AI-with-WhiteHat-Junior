# Write your code to increment a number by 50.

# Step 1: Ask the user to enter the first number as an integer and then store it in a variable num.
num = int(input("Enter an integer number : "))

# Step 2: Create a function and name it 'increment()' which takes one input 'n'.
def increment(n):
  
# Step 3: Add the input parameter 'n' with 50 using the '+' operator and store the result in a variable.
  result = n + 50
  
# Step 5: Print the result in the output using the 'return' keyword.
  return result
	  
# Step 5: Call the 'increment()' function and pass the variable 'num' as an input.
increment(num)
