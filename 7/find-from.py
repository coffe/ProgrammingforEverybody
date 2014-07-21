#-*-coding:utf-8-*-

# En loop som öppnar filen mbox-short.txt och letar i varje linje efter "From:".
# När From: hittas printar den ut det men jag har även lagt till en räknare 
# som räknar hur många linjer det blir och printar ut talet framför varje rad den printar.

ffind = open("mbox.txt")
count = 0
for line in ffind:
	line = line.rstrip() #( Denna linje tar bort tomrum i slutet av varje linje som hittas ÄVEN "newline")
	if line.startswith("From:"):
		count = count + 1
		print count, line