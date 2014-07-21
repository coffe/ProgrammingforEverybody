#-*-coding:utf-8-*-

#grund = raw_input("Procent av?: ")
#proc = raw_input("Vilket procent vill du veta?: ")
#grundconv = int(grund)
#procconv = (proc)
#resultat = grundconv * procconv
#convres = int(resultat)
#print convres


grund = raw_input("Procent av?: ")
proc = raw_input("Vilket procent vill du veta?: ")
convres = int(grund) * int(proc) #på någpt sätt måste jag få python att själv lägga in "0." innan proc:en
print float(convres)