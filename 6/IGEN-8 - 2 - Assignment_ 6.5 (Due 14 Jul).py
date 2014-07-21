#-*-coding:utf-8-*-

data = "from kristofer.bratt@gmail.com sat jan 09:13:16 2014"
atpost = data.find("@")
print "Snabel-a:",atpost
spacepos = data.find(" ",atpost)
print "space:",spacepos
host = data[atpost+1:spacepos]
print "host-name is:",host