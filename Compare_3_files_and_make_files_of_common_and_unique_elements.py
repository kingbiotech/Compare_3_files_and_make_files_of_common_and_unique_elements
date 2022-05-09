#!/usr/bin/python3
__author__ = "Dr. Kamlesh K. Sahu"
__version__ = "v 0.2"


os1a = input("Enter first file  - ")
os1af = os1a.split(".")
os1  = open(os1a)
os2a = input("Enter second file - ")
os2af = os2a.split(".")
os2  = open(os2a)
os3a = input("Enter third file  - ")
os3af = os3a.split(".")
os3  = open(os3a)

cm12  = open("Common_in_" + os1af[0] +"-"+ os2af[0] +".txt", "w")
cm23  = open("Common_in_" + os2af[0] +"-"+ os3af[0] +".txt", "w")
cm13  = open("Common_in_" + os1af[0] +"-"+ os3af[0] +".txt", "w")
cm123 = open("Common_in_" + os1af[0] +"-"+ os2af[0] +"-"+ os3af[0] +".txt", "w")

unique1  = open("Unique_in_"+os1af[0]+".txt", "w")
unique2  = open("Unique_in_"+os2af[0]+".txt", "w")
unique3  = open("Unique_in_"+os3af[0]+".txt", "w")

l1 = [];l2 = [];l3 = []

common12 = []
common23 = []
common13 = []
common123 = []

total12 = [];total23 = [];total13 = []

u1 = [];u2 = [];u3 = []


for line in os1:
	l1.append(line.strip())

for line in os2:
	l2.append(line.strip())

for line in os3:
	l3.append(line.strip())

#print("Common lines =======================================")
for i in l1:
	if i in l2:
		common12.append(i)
		cm12.write(i)
		cm12.write("\n")

for i in l2:
	if i in l3:
		common23.append(i)
		cm23.write(i)
		cm23.write("\n")

for i in l1:
	if i in l3:
		common13.append(i)
		cm13.write(i)
		cm13.write("\n")

for i in common12:
	if i in l3:
		common123.append(i)
		cm123.write(i)
		cm123.write("\n")
#print("Common lines Done===================================")

#print("Unique lines =======================================")

total12 = l1+l2
total23 = l2+l3
total13 = l1+l3

for i in l1:
	if i not in total23:
		u1.append(i)
		unique1.write(i)
		unique1.write("\n")

for i in l2:
	if i not in total13:
		u2.append(i)
		unique2.write(i)
		unique2.write("\n")

for i in l3:
	if i not in total12:
		u3.append(i)
		unique3.write(i)
		unique3.write("\n")

#print("Unique lines Done===================================")


print("----------------------------------------------------------------------------")
print("Common in \""+ os1a +"\" and \""+ os2a + "\" are ->", len(common12))
print("Common in \""+ os2a +"\" and \""+ os3a + "\" are ->", len(common23))
print("Common in \""+ os1a +"\" and \""+ os3a + "\" are ->", len(common13))
print("Common in \""+ os1a +"\" and \""+ os2a + "\" and \""+ os3a + "\" are ->", len(common123))
print("----------------------------------------------------------------------------")
print("Unique in \""+ os1a +"\" but not present in \""+ os2a + "\" and \""+ os3a +"\"are ->", len(u1))
print("Unique in \""+ os2a +"\" but not present in \""+ os1a + "\" and \""+ os3a +"\"are ->", len(u2))
print("Unique in \""+ os3a +"\" but not present in \""+ os1a + "\" and \""+ os2a +"\"are ->", len(u3))
print("----------------------------------------------------------------------------")
print("check output files in the same folder\nDone")


os1.close()
os2.close()
os2.close()
cm12.close()
cm23.close()
cm13.close()
cm123.close()
unique1.close()
unique2.close()
unique3.close()
