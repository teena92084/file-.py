d=open("teena.text","w")
a=d.write("teena ek achi ladki hai or use gussa bhot aatha hai")
print(a)
d=open("teena.text","a")
d.write("jun me mere exja hai")
d=open("teena.text","w+")
d.write("karina samjdar ladki hai")
print(d.read())
d.close()

