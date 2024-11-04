mayan_date = input("Enter mayan date")

mayan_date_list = mayan_date.split(" ")

baktun, katun, tun, unial, kin = int(mayan_date_list[0]), int(mayan_date_list[1]), int(mayan_date_list[2]), int(mayan_date_list[3]), int(mayan_date_list[4])

print(baktun)
print(katun)
print(tun)
print(unial)
print(kin)

kindays = kin
unialdays = unial * 20
tundays = tun *20 * 18
katundays = tun * 20 * 18 * 20
baktundays = tun * 20 * 18 * 20 * 20

print("------------------------------------")
print(kindays)
print(unialdays)
print(tundays)
print(katundays)
print(baktundays)
print("------------------------------------")

days = kindays + unialdays + tundays + baktundays + katundays

print(days)

baseyear = 2000
basemonth = 1
baseday = 1

def leap_year(year):
    year = year / 4
    yearstring = str(year)
    yearlist = yearstring.split(".")
    if yearlist[1] == "0":
        return True
    else:
        return False

daysinyear = 365
daysinleapyear = 366
mayandaysatbase = 1061243

while days >= daysinleapyear:
    if leap_year(baseyear):
        baseyear += 1
        days -= daysinleapyear
    else:
        baseyear += 1
        days -= daysinyear

print(baseyear)

while days >= daysinleapyear:
    if leap_year(baseyear):
        baseyear += 1
        days -= daysinleapyear
    else:
        baseyear += 1
        days -= daysinyear