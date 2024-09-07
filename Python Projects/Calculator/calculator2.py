def add(*args): #*args using it we can take as many arguments as one wants
    return sum(args) #sum is built in function to calculatae the sum

def subtract(*args):
    result = args[0] #letting the result be the first number of the argument
    for i in args[1:]: #using loop in the arguments except the first argument
        result -= i #subtracating the all the other elements from the first one
    return result #total subtracted value is returned 

def product(*args):
    result = 1 #assinging the value 1
    for num in args: #multiplying each nnumber with the one another in loop
        result *=num 
    return result

def divide(*args):
    if 0 in args[1:]: #if any number s=is divided by zero it is not possible
        return "It is not possible"
    result = args[0] # first argument is taken as numerator
    for num in args[1:]: #result is divided by other number
        result /= num
    return result

print("Calculator v2 \n")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.End\n")
while True:
    choice=input("Choose an option from above:")
    
    if choice in ('1','2','3','4','5'):
    
      if choice =='5':
          print("You have sucessfully exited")
          break
      num_list=[]
      
      while True:
         num = input("Enter anumber or 'done'to finish :")
         if num.lower() == 'done':
             break
         num_list.append(float(num))
         
      if choice == '1':
          print(f"\nThe sum of { '+'.join(map(str,num_list))} is {add(*num_list)}")
      elif choice == '2':
          print(f"\nThe difference of {'-'.join(map(str,num_list))}is {subtract(*num_list)}") #str converts num list to string cause number cannot be joined with string
      elif choice =='3':
          print(f"\nThe product of {'x'.join(map(str,num_list))} is {product(*num_list)}")
      elif choice == '4':
          print(f"\nThe division of given numbers is {'/'.join(map(str,num_list))} is {divide(*num_list)}")
      else:
          print("Invalid Input")

