#CTI-110
#P3T1 -AreasofRectangles
#Quinton Smith
#9/25/2019


#Input the length and width of rectangle 1
#Input the length and width of rectangle 2
#Calculate the are of rectangle 1.
#Calculate the are of rectangle 2.
#if area1 > area2
    #Display "Rectangle 1 has the greatest area."
#else if area2 > area1
    #Display "Rectangle 2 has the greatest area."
#else
    #Display"Both rectangles have the same area"

# Input the length and width of rectangle 1
length1 = int (input('Enter the length of rectangle 1:'))
width1 = int(input('Enter the width of rectangle 1:'))

# Input the length and width of rectangle 2
length2 = int (input('Enter the length of rectangle 2'))
width2 = int (input('Enther the width of rectangle 2'))

# Calculate the areas of the rectangles.
area1 = length1 * width2
area2 = length2 * width2

# Determin which has the greater area.
if area1 > area2:
    print('Rectangle 1 has the greater area.')
elif area2 > area1:
    print('Rectangle 2 has the greater area.')
else:
    print ('Both have the same area.')
