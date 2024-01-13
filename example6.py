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
def month_of_year(year, month):
    months=["January","February","March","April","May","June","July","August","September","October","November","December"]
    return months[month-1]

def days_of_week(year,month,day):
    if year < 1582 and month <1 or month >12:
        return None
    days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    if month==1 or month==2:
        year=year-1
        month=month+12
    return days[(year+year//4-year//100+year//400+(13*month+8)//5+day)%7]
days_of_week(2023,2,6)
def main():
    year=int(input("Enter year: "))
    month=int(input("Enter month: "))
    day=int(input("Enter day: "))
    print(f"{month_of_year(month)} {year} has {days_of_month(year,month)} days")
    print(f"{days_of_week(year, month, day)}")
