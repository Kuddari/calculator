"""
Program: Simple Calculator 
Author: Kuddari
Simple calcuatro help the user calculate the basic 4 operations including:
addition, subtraction, multiplication and division
Significant constants
         there is no constants
 2. The inputs are
         2 numbers (at least)
 3. Computations:
         addition: number + another number
         subtraction: number - another number
         multiplication: number * another number
         division: number / another number
 4. The outputs are
         computation result
"""

total = 0
cul = True
user = input('Please enter your name :')
while cul == True:
      operation = str(input('Please type in the math operation you would like to complete: '))
        
      try:
           number = int(input("Put your number: "))
           if number == isinstance(number,int):
                  break
                  
      except ValueError:
            print('Hey',user,',you must enter a number')
            continue
            

      if operation == '+':
            print('{} + {}  '.format(total, number),'= ', total + number)

            total = total + number
      elif operation == '-':
            print('{} - {}  '.format(total, number) ,'= ',(total - number))
            total = total - number

      elif operation == '*':
            print('{} * {}  '.format(total, number) ,'= ',(total * number))
            total = total * number
      elif operation == '/':
            print('{} / {}  '.format(total, number) ,'= ',(total / number))
            total = total / number


      else:
            print('You have not typed a valid operator, please run the program again.')
     
      answer = input('''If you want to continue press 'Y' 
      If you want to stop press 'N' : ''')
      if answer =='Y':
            cul = True
      else:
            cul = False
print(user,',your final result is ', total)
print('Thank YOU SO MUCH FOR USING MY SIMPLE PROGRAM,',user)
