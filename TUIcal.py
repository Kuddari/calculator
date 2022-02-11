import sys

result = 0
num_1 = 0
num_2 = 0
new_num = 0

def num1 ():
    global num_1
    try:
        num_1 = float(input('Put your first number : '))
        if num_1 == isinstance(num_1,float):
            num1()

    except ValueError :
        print('you must enter a number!!')
        

def num2():
    global num_2
    try:
        num_2 = float(input('Put your second number : '))
        if num_2 == isinstance(num_2,float):
            num2 ()
    except ValueError :
            print('you must enter a number!!')

def newnum ():
    global new_num
    try:
        new_num = float(input('Put your number : '))
        if new_num == isinstance(new_num,float):
            newnum ()
    except ValueError :
            print('you must enter a number!!')
            
 
def oprt():
    global result
    operation = input("Select operator '+' , '-' , '*' , '/' : ")
    if (operation == '+' or operation == '-' or operation == '*' or operation == '/'):
        if operation == '+':
            if result <= 0 :
                print('{} + {} '.format(num_1, num_2),'= ', "{:.2f}".format(num_1 + num_2))
                result = num_1 + num_2
            else :
                print('{} + {} '.format(result, num_2),'= ', "{:.2f}".format(result + num_2))
                result = result + num_2
            
        elif operation == '-':
            if result <= 0 :
                print('{} -{} '.format(num_1, num_2),'= ', "{:.2f}".format(num_1 - num_2))
                result = num_1 - num_2
            else :
                print('{} - {} '.format(result, num_2),'= ', "{:.2f}".format(result - num_2))
                result = result - num_2

        elif operation == '*':
            if result <= 0 :
                print('{} * {} '.format(num_1, num_2),'= ', "{:.2f}".format(num_1 * num_2))
                result = num_1 * num_2
            else :
                print('{} * {} '.format(result, num_2),'= ', "{:.2f}".format(result * num_2))
                result = result * num_2
        elif operation == '/':
            if result <= 0 :
                print('{} / {} '.format(num_1, num_2),'= ', "{:.2f}".format(num_1 / num_2))
                result = num_1 / num_2
            else :
                print('{} / {} '.format(result, num_2),'= ', "{:.2f}".format(result / num_2))
                result = result / num_2
    else :
        print ("You must input operation value!!")
        oprt ()

def calculation ():
    num1 ()
    num2 ()
    oprt ()
    addcal ()

def continuecal ():
    newnum ()
    oprt ()
    addcal ()

def addcal ():
    add = input ("""if you want to add more operation 'Y' 
if you want to stop 'N': """)
    
    if add.upper() == 'Y':
        continuecal ()
    else:
        sys.exit("You're welcome,see you again")




calculation ()




