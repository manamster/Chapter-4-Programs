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
# Markup Program 
# 11/30/2020 

#Step 1: Make the tupules
toys = ("Teddy Bear", "Toy Train", "Hula Hoop", "Betsy Wetsy", "Pogo Stick")
basePrice = (12.50, 58.75, 10, 15, 11)

#Step 2: Print the header
print("{:<15}{:<10}{:<10}{:<10}".format("Item", "Cost", "Markup", "Retail"))

#Step 3: Make the for loop
for i in range(0, len(toys)):
  #Step 3.1: do the calculations for the varaiables
  markup = 0.4 * basePrice[i]
  retail = markup + basePrice[i]
  #Step 3.2: Print the final result
  print("{:<15}{:<10.2f}{:<10.2f}{:<10.2f}".format(toys[i], basePrice[i], markup, retail))