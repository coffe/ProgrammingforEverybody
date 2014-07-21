#-*-coding:utf-8-*-
try:
    inp = raw_input("Enter Hours: " )
    hours = float(inp)
    inp = raw_input("Enter Rate: ")
    rate = float(inp)
except:
    print "Error, pleas enter numeric input"
    quit() #dödar programmet efter detta på ett "snyggt sätt#"

#print rate, hours
if hours <= 40 :
        pay = rate * hours
else :
        pay = rate * 40 + (rate * 1.5 * ( hours - 40) ) 
print pay