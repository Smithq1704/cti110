#CTI-110
#P3HW1-Month Number
#Quinton Smith
#9/25/2019

# Program is to prompt the user to enter the month's number (1 through 12)
#The program should display the name of the month's number that was entered.
#If the number is outside of the range of 1 through 12, the program should display an errormessage.



#Input month numbers using boolean method displaying the names as well
#input 'else' command
#output month names

inputmonth = (int(input("Enter months number 1-12: ")))

if inputmonth == 1:
    print ("January.")

elif inputmonth == 2:
    print ("February")

elif inputmonth == 3:
    print ("March")

elif inputmonth == 4:
    print ("April")

elif inputmonth == 5:
    print ("May")

elif inputmonth == 6:
    print ("June")

elif inputmonth == 7:
    print ("July")

elif inputmonth == 8:
    print ("August")

elif inputmonth == 9:
    print ("September")

elif inputmonth == 10:
    print ("October")

elif inputmonth == 11:
    print ("November")

elif inputmonth == 12:
    print ("December")

elif inputmonth == 0:
    print ("Incorrect input")

else:
    print ("Incorrect input!")
