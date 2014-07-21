#-*-coding:utf-8-*-

x = "X-DSPAM-Confidence:    0.8475";
pos = x.find(":")
num = float(x[pos+1:])
print num




#-*-coding:utf-8-*-
#
#x = "X-DSPAM-Confidence:    0.8475";   (stringen dönas in i x)
#pos = x.find(":")                      (vi söker efter : i stringen x och knör in resultatet i pos)
#xfloat = x[pos+1:]                     (sedan tvättar vi bort / hoppar fram ett steg så att vi säller oss efter ":" samt slänger in de resultatet i pos)
#num = float(xfloat)                    (Nu när vi bara har siffror kan vi konvertera strängen till en float och knö in resultatet i num )
#print num
