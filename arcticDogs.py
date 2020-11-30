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
# Arctic Dogs Program 
# 11/30/2020 

#Step 1: Input the tupules
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
numSold = (28,30,24,10,12,10,5,3,4,10,21,25)

#Step 2: Print the header
print("{:<20}{:<20}".format("Month", "Sales"))
#Step 3: Create the for loop
for i in range(0, len(months)):
  #Step 3.1: Print the month and the sales for that month
  print("{:<15}".format(months[i]), end="")
  print("*" * numSold[i])