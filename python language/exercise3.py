current_age=int(input("enter your age"))
day=(90*365)-(current_age*365)
month=(90*12)-(current_age*12)
weeks=(90*52)-(current_age*52)
if current_age<=90:
    print(f"we have{day}days and{month} months and {weeks} weeks")
    #or we done in another way also
current_age=int(input("enter your age"))
years_left=90-current_age
months=years_left*12
weeks=years_left*52
days=years_left*365
print(f"we have{days}days and{months} months and {weeks} weeks")

