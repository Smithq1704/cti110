




score = float (input("Input Grade:"))

A_score = 90
B_score = 80
C_score = 70
D_score = 60




if score >= 101:
    print ("error")

if score >= A_score and score <= 100:
    print ("Your grade is A.")

elif score >= B_score:
    print ("Your grade is B.")

elif score >= C_score:
    print ("Your grade is C")

elif score >= D_score:
    print ("Your grade is D")

else:
    print ("Your grade is F")
    
