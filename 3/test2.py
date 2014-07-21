#3.3 Write a program to prompt the user for a score 
#using raw_input. Print out a letter grade based on 
#the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a 
#suitable error message and exit. For the test, 
#enter a score of 0.85
#
#-*-coding:utf-8-*-

try:
    inp = raw_input("Enter your score, please: " )
    usersc = float(inp)

    if usersc >= 0.9 :
        print "A"
    elif usersc >= 0.8 :
        print "B"
    elif usersc >= 0.7 :
        print "C"
    elif usersc >= 0.6 :
        print "D"
    elif usersc < 0.6 :
        print "F"
    else :
        print "Score out of range"

#    inp = raw_input("Enter Rate: ")
#   rate = float(inp)
except:
    print "Error, pleas enter numeric input"