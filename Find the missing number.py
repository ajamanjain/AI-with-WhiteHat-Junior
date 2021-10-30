# Write a program to find the missing number in the list
def missing_num(list):
  for n in range(1,11):
    if n not in list:
      print(n)

missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10])
missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8])
missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9])
