# first program in python
# input two numbers, add them together, print them out
# wfp, 9/1/07; rje, 5/5/14


# defining the answer
answer = 194

#start game
p =  '\n\
I am a three-digit number.\n\
My tens digit is 5 more than my ones digit.\n\
My hundreds digit is 8 less than my tens digit.\n\
What number am I?\n\
'

print(p)

num_str1 = input('Please enter an integer: ')
int_var = int(num_str1)

while (int_var != answer):
    print('try again')
    print(p)
    num_str1 = input('Please enter an integer (hundreds digit): ')
    
input('You WIN!!')

    
