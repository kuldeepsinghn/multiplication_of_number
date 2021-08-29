def leap_year():
    year = 2021
    if (year % 4) == 0:
        print(year, "is a leap year")
    elif (year % 100) == 0:
        print(year, "is a leap year")
    elif (year % 400) == 0:
        print(year, "is a leap year")
    else:
            print(year, "is not a leap year")
    
    
    
    
if __name__ == '__main__':
    leap_year()

