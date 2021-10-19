# Write your code here

# Step 1: Get the user input
num = int(input("Enter the integer no. to get the table of : "))

# Step 2: Initialize variable 'i' with value '1'
i = 1

# Step 3: Execute a 'while' loop 10 times 
while i<11:
  
# Step 4: Multiply the 'num' variable with 'i' variable and store in 'multiply' variable.
  multiply = num * i
  
# Print the result stored in the `multiply` variable 
  print(num, " x ", i, " = ", multiply)
  
# Increment the value of 'i' by 1
  i += 1
