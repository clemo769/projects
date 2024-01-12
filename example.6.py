def check_leap_year(year):
    if year % 4==0 and (year % 100!=0 or year % 400 == 0):
        return True
    else:
        return False
def days_of_month(year,month):
    if year < 1582 and month <1 or month >12:
        return None    
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    res=days[month-1]
    if month==2 and check_leap_year(year):
        res=29
    return res
def month_of_year(year):
    months=["January","February","March","April","May","June","July","August","September","October","November","December"]
    return months[month-1]
year=int(input("Enter a year: "))
month=int(input("Enter a month: "))
print(f"{month_of_year(month)} {year} has {days_of_month(year,month)} days")  