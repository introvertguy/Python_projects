choice = 'random'

def line():
    print('---------------------')


def show_menu():
    print("Operation Menu")
    line()
    print('1.Addition')
    print('2.Subtraction')
    print('3.Multiplication')
    print('4.Division')
    print('5.Comparison')
    print('6.Exit')
    line()
    user_ip = input('Enter your choice of operation: ')
    return user_ip


num1 = input("Enter a number: ")
num2 = input("Enter another number: ")



while choice!=6 :
    choice = show_menu()
    if(choice == '1'):
            item = float(num1) + float(num2)
            print("Addition is ",item)
        
    elif(choice =='2'):
            item = float(num1) - float(num2)
            print("Subtraction is ",item)
    
    elif(choice =='3'):
            item = float(num1) * float(num2)
            print("Multiplication is ",item)
        
    elif(choice =='4'):
            item = float(num1) / float(num2)
            print("division is ",item)
        
    elif(choice =='5'):
        
        
        if(float(num1) > float(num2)):
            item = float(num1)
            print("The greater number is: ",item)
            item = float(num2)
            print("The smaller number is: ",item)
        else:
            item = float(num2)
            print("The greater number is: ",item)
            item = float(num1)
            print("The smaller number is: ",item)
        
    elif(choice =='6'):
        print('Goodbye')
        
    else:
        print('Please enter one of 1, 2, 3, 4, 5, 6')
