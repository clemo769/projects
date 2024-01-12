def leap_year_function(n):
    leap_year= 2020
    if leap_year + 4 == n :
        n=leap_year
        print("The year",n, "is a leap year.")
    else:
        leap_year_function(int(input("Enter a value: ")))
leap_year_function(2016)