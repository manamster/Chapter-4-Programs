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
# Tpying Program ⌨️
# 11/30/2020 

#Step 1: Input the names of the sudents
students = ("Grumpy", "Dopey", "Doc", "Happy", "Bashful", "Sneezy", "Sleepy")
#Step 2: Print the header
print ("Welcome to the Typing Program!  ")
#Step 3: Create the for loop
for i in range(0, len(students)):
  #Step 3.1: Get the wpm of each student
  wpm = int(input("How many words per minute can "+ str(students[i]) +" type? "))
  if wpm >= 25:
    #Step 3.2.1: If the wpn are greater than or equal to 25 they pass
    print(str(students[i]) + " you are typing fast enough to pass keyboarding.\n")
  else: 
    #Step 3.2.2: If not then they fail
    print("Sorry, "+str(students[i]) + " you need to type faster to pass Keyboarding.\n")