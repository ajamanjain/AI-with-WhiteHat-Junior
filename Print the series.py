# Write your solution here
# Step 1: Create a function 'series(n)'
def series(n):
  # Step 2: Initialize 'n1' and 'n2' variables
  n1 = 0
  n2 = 1
  # Step 3: Initialize 'count' variable
  count = 0
  
  # Step 4: Check whether 'n'<=0
  if n<=0:
    print("Please enter a positive intteger")
  else:
    # Step 5: Run a while loop till 'count' < 'n'
      while count<n:
    # Perform Step 6 
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
# Step 7: Call 'series()' function
series(10)
