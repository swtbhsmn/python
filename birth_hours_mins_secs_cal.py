from datetime import date

def convert_birthdate(year_of_birth,month_of_date,date_of_birth):
    today = date.today()
    years = today.year - year_of_birth \
            - ((today.month, today.day) < (month_of_date, date_of_birth))
    return years*365.25*24, years*365.25*24*60, years*365.25*24*3600

hours, minutes ,seconds = convert_birthdate(1998,3,17)

print("I'm Swetabh Suman. I have spend approx {} hours!.\n\
In terms of #minutes and #seconds is {} &{}.\n\
According to Julian year (1 year = 365.25 days). It is used for astronomical calculations.".format(hours,minutes,seconds))

#==================Output========================
#I'm Swetabh Suman. I have spend approx 192852.0 hours!.
#In terms of #minutes and #seconds is 11571120.0 &694267200.0.
#According to Julian year (1 year = 365.25 days). It is used for astronomical calculations.
