# Do you really need an explaination for this?
import math

# Input year in sections of two digits, the century digits and the year digits
# Century digits are input as an integer, year digits are input as string
# and later converted to integer, because an input as 00 (zero zero) would be
# shortened to 0 (zero)
# Only works with 4-digit years, in 2 digit parts. The program checks this!
def DigitInput():
    global century_digits_int
    global year_digits_str
    global year_digits_int
    century_digits_int = input ("Enter the first two digits of the year: ")
    while len(str(century_digits_int)) != 2:
        century_digits_int = input ("This script only supports years with 4 digits! \nPlease try again for the first two digits: ")
    year_digits_str = raw_input ("Enter the last two digits of the year: ")
    year_digits_int = int(year_digits_str)
    while len(year_digits_str) != 2:
        year_digits_str = raw_input ("This script only supports years with 4 digits! \nPlease try again for the last two digits: ")
    return CenturyCalc(), century_digits_int, year_digits_int, year_digits_str


# Determines whether the century is 18xx or 20xx
# and declares value variable
def CenturyCalc():
    global value
    value = year_digits_int + math.floor(year_digits_int/4)
    if century_digits_int == 18:
        value += 2
    elif century_digits_int == 20:
        value += 6
    return IsLeapYear(), value


# Determines whether a given year is a leap year
# Also further trickery with converting ints to strings and vice versa
def IsLeapYear():
    global leap_year
    year_total_str = str(century_digits_int) + year_digits_str
    year_total_int = int(year_total_str)
    print ("Entered year: " + year_total_str)
    if year_total_int % 4 == 0 and year_total_int % 100 != 0:
        leap_year = True
    elif year_total_int % 400 == 0:
        leap_year = True
    else:
        leap_year = False
    print ("Is the given year a leap year? " + str(leap_year))
    return DetermineMonth(), leap_year


# Determining the month and add appropriate int to value-variable
# Also determines how many days are in each month, for use in DetermineDay()
def DetermineMonth():
    global value
    global days_in_month
    month_valid = False
    while month_valid == False:
        month_str = raw_input("What month are we talking about? ").lower() # If the program does not recoginise raw_input, change to input (bug)
        if month_str == "january":
            month_valid = True
            if leap_year == True:
                print ("") # Prints nothing, so the progam doesn't crash because of an indentation error
                # nothing here
            elif leap_year == False:
                value += 1
            days_in_month = 31
        elif month_str == "february":
            month_valid = True
            if leap_year:
                value += 3
                days_in_month = 29
            else:
                value += 4
                days_in_month = 28
        elif month_str == "march":
            month_valid = True
            value += 4
            days_in_month = 31
        elif month_str == "april":
            month_valid = True
            print ("") # Prints nothing, so the progam doesn't crash because of an indentation error
            # nothing here
            days_in_month = 30
        elif month_str == "may":
            month_valid = True
            value += 2
            days_in_month = 31
        elif month_str == "june":
            month_valid = True
            value += 5
            days_in_month = 30
        elif month_str == "july":
            month_valid = True
            print ("") # Prints nothing, so the progam doesn't crash because of an indentation error
            # nothing here
            days_in_month = 31
        elif month_str == "august":
            month_valid = True
            value += 3
            days_in_month = 31
        elif month_str == "september":
            month_valid = True
            value += 6
            days_in_month = 30
        elif month_str == "october":
            month_valid = True
            value += 1
            days_in_month = 31
        elif month_str == "november":
            month_valid = True
            value += 4
            days_in_month = 30
        elif month_str == "december":
            month_valid = True
            value += 6
            days_in_month = 31
        else:
            print ("Invalid month is entered!")
            month_valid = False

    return DetermineDay(), value,days_in_month


# Determining the day, calculating the final value and printing the day of the week.
def DetermineDay():
    global days_in_month
    day_int = int(input("What is the date of that day? "))
    while not 1 < day_int < days_in_month:
        day_int = int(input("Invalid date entered! Try again: "))
    day_value = (value + day_int) % 7
    if day_value == 1:
        day_str = "Sunday"
    elif day_value == 2:
        day_str = "Monday"
    elif day_value == 3:
        day_str = "Tuesday"
    elif day_value == 4:
        day_str = "Wednesday"
    elif day_value == 5:
        day_str = "Thursday"
    elif day_value == 6:
        day_str = "Friday"
    elif day_value == 0:
        day_str = "Saturday"
    else:
        print ("Error: value not in range for day calculation")
        day_str = "Error!"
    print ("The day of the week for the date that you entered is a " + day_str + ".")
    return StartOver()

# Asks user if he want's to restart the program and does so if "y" is entered.
# If "n" is entered, program exits. If answer is invalid, asks again.
def StartOver():
    start_over = raw_input("Do you want to restart the program? y/n: ")
    if start_over == "y":
        DigitInput()
    elif start_over == "n":
        print ("Exiting...")
    while start_over != "y" and start_over != "n":
        start_over = raw_input("Please choose: y/n: ")
        if start_over == "y":
            binary_input()
        elif start_over == "n":
            print ("Exiting...")

# Starts the program for the first time
DigitInput()
