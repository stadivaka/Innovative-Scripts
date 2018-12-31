#/usr/bin/python
'''
DB table created based on pincodes
https://raw.githubusercontent.com/kishorek/India-Codes/master/csv/pincodes.csv
'''
_author_ = "Surya Tadivaka"

import sqlite3

conn = sqlite3.connect('India_Zip_Codes.sqlite')
cur=conn.cursor()

cursor = conn.execute("SELECT PostOfficeName, Pincode, DistrictsName, City, State  from pincodes")
for row in cursor:
   print ("PostOfficeName = ", row[0])
   print ("Pincode = ", row[1])
   print ("DistrictsName = ", row[2])
   print ("City = ", row[3])
   print ("State = ", row[4], "\n")

print ("Operation done successfully")
conn.close()
