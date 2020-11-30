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
# Backwards Message Program 🤖
# 11/30/2020 

#Step 1: get the phrase from the user
phrase = str(input("What is the phrase you want to input? \n"))
#Step 2: Make the for loop that goes from the last letter to the first
for i in range(len(phrase)-1, -1, -1):
  #Step 2.1: print each letter with an ending of nothing
  print(phrase[i], end="")