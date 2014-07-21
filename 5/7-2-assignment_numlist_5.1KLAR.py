Maximum = None
Minimum = None
while True:
    inp = raw_input("Enter a number: ")
    if inp == "done" : break
    if len(inp) < 1 : break


    try:
        num = float(inp)
    except:
        print "Invalid input"
        continue

  
    if Minimum is None:
        Minimum = inp
    elif inp < -1:
        Minimum = inp



    if Maximum is None:
        Maximum = inp
    elif inp > Minimum:
        Maximum = inp


print "Maximum is",Maximum
print "Minimum is",Minimum


