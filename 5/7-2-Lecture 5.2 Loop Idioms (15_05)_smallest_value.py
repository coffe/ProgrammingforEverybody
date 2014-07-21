#-*-coding:utf-8-*-
minst = None
print "Before"
for value in [9,41,12,3,74,15]:
    if minst is None:
        minst = value
    elif value < minst:
        minst = value
    print minst, value

print "after", minst

#minst = None
#print "Before"
#for värde in [9,41,12,3,74,15]:
#    if minst is None:
#        minst = värde
#    elif värde < minst:
#        minst = värde
#    print minst, värde
#
#
#print "after", minst