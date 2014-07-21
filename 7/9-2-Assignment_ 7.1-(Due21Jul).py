#-*-coding:utf-8-*-

fname = raw_input("Enter a file name: ")
if len(fname) == 0:
	fname ="mbox-short.txt"
fhand = open(fname)
for line in fhand :
	line = line.rstrip().upper() #man kan slänga på flera ändringar
#	line = line.upper()
	print line
#fname = open("mbox-short.txt")
#count = 0
#for line in fname:
#	line = line.rstrip() #( Denna linje tar bort tomrum i slutet av varje linje som hittas ÄVEN "newline")
#	if line.startswith("From:"):
#		count = count + 1
#		print line