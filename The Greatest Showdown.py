#Task 1: Identify the Greatest Write a Python program that prompts the user to enter three numbers. The program should then identify and print out the largest number among the three.
value_1=int(input (" Enter value one  "))
value_2=int(input( " Enter value two  "))
value_3=  int(input (" Enter value three  ")) 
largest_num= value_1, value_2, value_3

x=value_1
y=value_2
z=value_3

if value_1 > value_2 and value_3:
    print  ((value_1), "is the largest number")
elif value_2 > value_1 and value_3:
    print( (value_2),"is the largest number")
elif value_3 > value_1 and value_2:
    print ((value_3)," is the largest number")

#Task 2: Identify the Smallest Extend your program from Task 1 to also determine the smallest number among the three and print it out.
    
if value_1 < value_2 and value_3:
    print  ( (value_1), "is the smallest number")
elif value_2 < value_1 and value_3:
    print ( (value_2), " is the smallest number")
elif value_3 <  value_1 and value_2:
    print ( (value_3), "is the smallest number")
    
#Task 3: Equality  Check Enhance your program to handle cases where two or all of the numbers are equal. The program should display appropriate messages like "Two numbers are equal and the largest" or "All numbers are equal".
    
if (value_1 and value_2 > value_3):
        print(( value_1, value_2), (" are larger than"), (value_3))
        
elif (value_2 and value_3 > value_1):
    print(( value_3, value_2), (" are larger than"), (value_1))
    
elif (value_3 and value_1 > y):
        print(( value_2, value_3), (" are larger than"), (value_2))
    
            



if value_1 == value_2:
    print  ( (value_1, value_2), " are equal numbers")
elif value_1 == value_3:
    print ( (value_1, value_3)," are equal numbers")
elif value_2==  value_1:
    print ( (value_1, value_3), " are equal numbers")
elif value_2==  value_3:
    print ((value_2, value_3)," are equal numbers")
elif value_3 ==  value_1:
    print ((value_1, value_3)," are equal numbers")
elif value_3==value_2:
    print ((value_2, value_3), " are equal numbers")
    
else:
    print (" Enter a Number")
    
    
    
    



    


