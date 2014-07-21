fname = raw_input("Enter file name: ")
if len(fname) == 0:
	fname ="mbox-short.txt"
#	print "filename is: ", fname
count = 0
total = 0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.strip()
    #print line
    pos = line.find(" ")
    num = float(line[pos+1:])
    count = count +1
    total = total + num 

	#print flyt
print "Average spam confidence: " , total / count