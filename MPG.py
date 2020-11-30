#  .&&&&&&&&&&&&&&&&&&                                
# ,&&&&&&*****&&&&&&&&&.                             
# ,&&&&&&*,,,,,,,&&&&&&&,                            
# ,&&&&&&*,      &&&&&&(*.                           
# ,&&&&&&*.     &&&&&&&*,.                           
# ,&&&&&&&&&&&&&&&&&&**,,                            
# ,&&&&&&&&&&&&&&&***,,.                             
# ,&&&&&&****&&&&&&&.                                
# ,&&&&&&*,..,&&&&&&&,                               
# ,&&&&&&*,   .,&&&&&&&.                             
# ,&&&&&&*.     .@&&&&&&&.                           
# ,@@&@&@*,      .,@@&@&@@@                          
#  ,******.        .,******,,     
# Calvin Comstock-Fisher and Vincent Staputis
# Miles Per Gallon Program 🚗
# 11/30/2020 

#Step 1: Prints the welcome statement
print("Welcome to the Miles Per Gallon program.")
#Step 2: Create the for loop
for i in range(1,52):
  #Step 2.1: Print the week based on the times repeated in the for loop
  print("Week " + str(i))
  #Step 2.2: Get the values from the user
  gallons = int(input("How many gallons of gas did you use this week? "))
  miles = int(input("How many miles did you drive this week?"))
  
  #Step 2.3: Calculate the mpg
  mpg = miles / gallons

  #Step 2.4: Print the results
  print("Your car got " + str(mpg) + "mpg during the week. \n")