'''#import csv module
import csv
#open csv file
file=open("example.csv","r")
#read the csv file
read=csv.reader(file,delimiter=',')
#output csv content
for row in read:
     print(row)
#close the file 
file.close()
'''
# write in csv file
import csv
# new record
rec=['1000','sunil','kanaujiya','IT']
#open the file
file=open("example.csv","a")
#write to the csv file
wrt=csv.writer(file)
#write a new record in the file
wrt.writerow(rec)
#close the file
file.close()
