from datetime import datetime
dob_input=input("enter your dob (dd-mm-yyyy):")
dob=datetime.strptime(dob_input,"%d-%m-%Y")
today=datetime.today()
age=today.year-dob.year
if (today.month,today.day)<(dob.month,dob.day):
    age-=1
print("you are", age, "years old")