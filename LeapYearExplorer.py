#Task 1: Leap Year CheckerWrite a Python program that prompts the user to input a year. The program should determine if the given year is a leap year or not and then display an appropriate message

leap_yr = int(input("Please Enter Year : "))

if (leap_yr%400 == 0):
    print("True: %d is a leap year" %leap_yr)
elif (leap_yr%100 == 0):
    print("False: %d is not a leap year" %leap_yr)
elif (leap_yr%4 == 0):
    print("True: %d is a leap year" %leap_yr)
else:
    print("False: %d is not a leap year" %leap_yr)