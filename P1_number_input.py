# first program in python

#start game with puzzle stored in variable p
p =  '\n\
I am a three-digit number.\n\
My tens digit is 5 more than my ones digit.\n\
My hundreds digit is 8 less than my tens digit.\n\
What number am I?\n\
'

# defining the answer of the puzzle
answer = 194
   
 
def main():
    'a guessing game that continues untill responded gives the correct answer'
    
    print(p)
    
    #this variable stores the respondends guess
    num_str1 = input('Please enter an integer: ')
    
    # loop until the right answer is given
    while num_str1 != answer:

        if num_str1 > answer:
            print('try again, answer is lower')  
            print(p)
            num_str1 = int(input('Please enter an integer: '))
            
        elif num_str1 < answer:
            print('try again, the answer is higher')
            print(p)
            num_str1 = int(input('Please enter an integer: '))
            
    print('You WIN!!')        

        
main()

    
