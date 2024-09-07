def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        return "It is not possible"
    
    else:
        return x/y
    
    
print("Calculator")
print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")

while True:
    choice = input("\nChoose a Number from above:\n")
    
    
    if choice in ('1','2','3','4','5'): #choice is string hence it can be equal to string only
        
       if choice == '5':
           print("You have exited the program")
           break
       num1=float(input("\nEnter a number:"))
       num2=float(input("Enter a second number:"))
       
       if choice =='1':
           print(f"\n{num1}+{num2}={add(num1,num2)}")
           
       
       elif choice =='2':
           print(f"\n{num1}-{num2}={subtract(num1,num2)}")
           
       
       elif choice =='3':
           print(f"\n{num1}x{num2}={multiply(num1,num2)}")
           
           
       elif choice == '4':
           print(f"\n{num1}/{num2}={divide(num1,num2)}") #parameter jasari pass garyo tesari nai jancha
           
           
    else:
          print("Invalid input")    
       
    
