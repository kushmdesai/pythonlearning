import csv

with open('coors.csv', mode='r',newline='') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        print(row['first_name'], row['last_name'])
with open('coors.csv', mode='a',newline='') as infile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(infile, fieldnames=fieldnames)
    wname = input('would you like to add your name?   (y/n): ').lower().strip() == 'y'
    if wname:
     fname=str(input("what is your first name:  "))    
     lname=str(input("what is your last name:  "))    
     writer.writerow({'first_name': fname , 'last_name': lname})
