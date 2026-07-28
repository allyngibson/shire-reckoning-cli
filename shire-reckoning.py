#!/bin/python3

# A little program to render the current date according to
# Shire Reckoning, the calendar in use by the Hobbits of
# JRR Tolkien's The Lord of the Rings, as described in
# Appendix D.

# Originally written in BASIC in the autumn of 1999, rewritten
# in PHP for a WordPress plugin in 2005, and rewritten again
# in Python in 2026.

# I use this pipe with cowsay:
#    python3 shire-reckoning.py | cowsay -f dragon
# A fire-breathing dragon (very Tolkien!) tells you the date
# Set up an alias in .bash_aliases like:
#    alias shire="python3 shire-reckoning.py | cowsay -f dragon"
# And you don't have to remember all that.

# Allyn Gibson
# July 28, 2026 / 8 Wedmath
# allyngibson.com

import datetime
from datetime import date

# Is this a leap year or no? Use the Gregorian calculation.
def is_leap_year(year):
    # Divisible by 4, but not 100 unless also divisible by 400
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def shire_day(day):
    shire_julian = int(day)+11
    if shire_julian > (365+leap):
        shire_julian = shire_julian - (365+leap)
    return shire_julian

# Define a dictionary of month names in use in the Shire in the late Third Age
months_list = ["Afteryule", "Solmath", "Rethe", "Astron", "Thrimidge", "Forelithe", "Afterlithe", "Wedmath", "Halimath", "Winterfilth", "Blotmath", "Foreyule", "Yule", "Lithe", "Midyear's Day", "Overlithe"]

# Define a dictionary of day names in use in the Shire in the late Third Age
days_list = ["Highday", "Sterday", "Sunday", "Monday", "Trewsday", "Hevensday", "Mersday"]

# Get today's date
today = date.today()

# Is this a leap year? We'll set a variable, because it's getting used
leap = 0
if is_leap_year(today.year) == True:
    leap = 1

# Counting forward from 2 Yule, what day of the year is this in the Shire?
shire_day_of_year = shire_day(today.strftime("%j"))

# Calculations! When are we in the Shire calendar?
shire_day = 0
shire_month = 0
# First, we take care of the days that are outside of the months
# 2 Yule
if shire_day_of_year == 1:
    shire_day = 2
    shire_month = 12
# 1 Lithe
if shire_day_of_year == 182:
    shire_day = 1
    shire_month = 13
# Mid-Year's Day
if shire_day_of_year == 183:
    shire_month = 14
# 2 Lithe
if shire_day_of_year == (184+leap):
    shire_day = 2
    shire_month = 13
# Overlithe (ie., Leap Day)
if shire_day_of_year == 184 and (leap == 1):
    shire_day = 0
    shire_month = 15
# 1 Yule
if shire_day_of_year == (365+leap):
    shire_day = 1
    shire_month = 12
# Hobbit months are 30 days each. We are going to remove the days
# that fall "outside" of months from out Shire Julian count, and then
# it's just a straight division by 30 for the month and a modulo
# (ie., remainder) for the day.
if shire_month == 0:
    modified_julian = shire_day_of_year - 1
    if modified_julian > (182+leap):
        modified_julian = modified_julian - (leap+3)
    shire_month = int((modified_julian - 1) / 30)
    shire_day = modified_julian % 30
    if shire_day == 0:
        shire_day = 30

# Calculate the day of the week. The Hobbit calendar had 52 weeks of 7
# days each, with Midyear's Day (and Overlithe) existing outside
# of the week. Thus, every year begins on Highday and ends of Mersday.
shire_day_of_week = 0
modified_julian = shire_day_of_year
if shire_day_of_year == 183 or (shire_day_of_year == 184 and leap == 1):
    shire_day_of_week = 7
if shire_day_of_week == 0:
    if shire_day_of_year > 183:
        modified_julian = shire_day_of_year - leap - 1
    shire_day_of_week = modified_julian % 7

# Output the Shire date
if shire_day > 0:
    # Works perfectly well 364 days of the year.
    print(f"{days_list[shire_day_of_week]}, {shire_day} {months_list[shire_month]} {today.year} CE")
else:
    # The case of the two days (Midyear's Day and Overlithe) that
    # exist outside of a week; these get just the day's designation.
    print(f"{months_list[shire_month]} {today.year} CE")
        


