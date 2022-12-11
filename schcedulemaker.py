import csv

with open('schedule.csv', mode='w',newline='') as infile:
    fieldnames = ['first_name','last_name','day_of_the_week','breakfast','lunch','snack','dinner']
    writer=csv.DictWriter(infile, fieldnames=fieldnames)
    writer.writeheader()
    wname = input('would you like to add your name?   (y/n): ').lower().strip() == 'y'
    if wname:
        fname = input('what is your first name?  ')
        lastName = input('what is your last name?  ')
        dotw = input('what is the day of the week?  ')
        bname = input('what will you be making for brakfast on this day?  ')
        lname = input('what will you be making for lunch on this day?  ')
        sname =input('what will you be making for snack on this day?  ')
        dname =input('what will you be making for dinner on this day?  ')
        writer.writerow({'first_name': fname , 'last_name': lastName , 'day_of_the_week':dotw , 'breakfast':bname ,'lunch':lname ,'snack':sname,'dinner':dname })