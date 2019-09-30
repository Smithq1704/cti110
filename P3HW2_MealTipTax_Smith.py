
# CTI-110
# P3HW2 - MealTipTax
# Quinton Smith
# 9/30/2019

# Only allow the input of 16, 18, 20%
# Else input error message and stop
# After input of 16, 18, 20% continue program
# Output meal tip and tax only for correct input


meal = float(input("Enter the charge for your meal  "))
print ("Meal %.2f" % meal)
#Ask user to enter the Tip for server in decimal format.
tip = float(input("Enter the Tip percentage for server 16%, 18% OR 20%  "))
tipAMT = (tip * meal)

if tip == 0.16 or tip == 0.18 or tip == 0.20:
    print ("Tip %.2f" % tip)
    print (tipAMT)
    tax = float (input ("Enter the tax amount in decimal format."))
    print ("Tax %.2f" % tax)

    taxAMT = (tax * meal)
    print (taxAMT)


    total = (taxAMT + meal + tipAMT)
    print ("Tip")
    print (tipAMT)
    print ("Tax")
    print (taxAMT)
    print ("Total $ %.2f" % total)

else:
    print ("error")
    






#Calculate tip and tax


#Display the following: Calculated tip, Calculate Tax, Display total cost of meal
