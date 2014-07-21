#-*-coding:utf-8-*-
count = 0
total = 0
while True:
    inp = raw_input("Enter a number: ")
        
    #Vad får vi från användaren?
    if inp == "done" : break
    if len(inp) < 1 : break #kollar efter tom linje
    
    #do the work
    try:
        num = float(inp)
    except:
        print "Invalid input"
        continue
    count = count + 1
    total = total + num
    print "Ditt nummer:",num,"Hur många tal:",count,"Totalt:",total

print "Averege:", total / count