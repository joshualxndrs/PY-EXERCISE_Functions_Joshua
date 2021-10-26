def convert_days():
    h = int(input("Input number of hours: "))
    m = int(input("Input number of minutes: "))
    s = int(input("Input number of seconds: "))

    total = get_days(h,m,s)
    print(f"The total number of days is: {total}")

def get_days(h,m,s):
    NumofDays = ((s/3600) + (m/60) + h) / 24

    return '%.4f'%NumofDays

convert_days()



#f"{total} days, {h} hours, {m} minutes, {s} seconds"