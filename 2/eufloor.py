s#-*-coding:utf-8-*-

# Ett skript som konverterar från europeiska våningar i hissen till amerikanska.
# Amerikanska hissar har inte våning 0 eller -0 Så som europa har.

inp = raw_input("Amerikansk våning? ") #Slänger upp en fråga om vilken amerikansk våning och fångar in svaret som användaren ger
euf = int(inp) - 1 #Konverterar "str"en (string) som svaret från användaren ovan blir till en int så att vi kan räkna med talet. Sedan subtraherar den en så att vi hamnar "en våning under"
print"EU floor", euf #printar EU floor plus summan av uträkningen i raden ovan