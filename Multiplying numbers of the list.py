# Write your code here
# Step 1: Define a list with some random numbers 
num_list = [2,3,7]
# Step 2: Get the length of the list using 'len()' function 
length = len(num_list)
# Step 3: Initialize two variables 'i' and 'result' 
i = 0
result = 1
# Step 4: Iterate while loop till the length of the list
while i<length:
  # Step 5: Multiply the 'result' variable with each element of the list. Use list indexing
  result *= num_list[i]
  # Increment 'i' variable
  i += 1
# Step 6: Print the result
print(result)
