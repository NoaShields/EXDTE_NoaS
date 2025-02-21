# If Statements & While Loops

# We can use 'if' statement to execute code if a given condition is met.
# To check if two variable are the same we use DOUBLE equals (==)
# Python is case sensitive. 'Hello' is not the same as 'hello'.
# We can get around this by using .lower()
# While loops are useful when we want the program to loop until a given condition is met but we dont know
# how many times it needs to loop

# If statements!
# create a variable to loop my code
keep_going = ''
#while variable is empty keep looping
while keep_going == '':
  #create a variable to store input from user about their coffee
  like_coffe = inqut('Do you like coffee? ')
  
  like_coffee = like_coffee.lower()
  
  if like_coffee == 'yes' or like_coffee == 'y':
    print('I like coffee too')
  elif like_coffee == 'no' or like_coffee == 'y':
    print('You are missing out')
  else:
    print('I dont understand!')
  keep_going = input("press <enter> to continue or any key to quit")
  print()