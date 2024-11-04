numberOfDays = 0
Year = 2000
Month = 1
Day = 1

baktun = int(input("Enter baktuns "))
numberOfDays += 20 * 20 * 18 * 20 * (baktun - 13)

katun = int(input("Enter katuns "))
numberOfDays += 20 * 18 * 20 * (katun - 20)

tun = int(input("Enter tuns "))
numberOfDays += 18 * 20 * (tun - 7)

uinal = int(input("Enter uinals "))
numberOfDays += 20 * (uinal - 16)

kins = int(input("Enter kins "))
numberOfDays += (kins - 3)

print(f"Number of days since 1 1 2000: {numberOfDays}")

while numberOfDays >= 31:
    if numberOfDays >= 31: 
        numberOfDays -= 31
        Month += 1
    if (Year % 4) == 0:
        if numberOfDays >= 29: 
            numberOfDays -= 29
            Month += 1
    else:
        if numberOfDays >= 28: 
            numberOfDays -= 28
            Month += 1
    if numberOfDays >= 31: 
        numberOfDays -= 31
        Month += 1
    if numberOfDays >= 30: 
        numberOfDays -= 30
        Month += 1
    if numberOfDays >= 31: 
        numberOfDays -= 31
        Month += 1
    if numberOfDays >= 30: 
        numberOfDays -= 30
        Month += 1
    if numberOfDays >= 31: 
        numberOfDays -= 31
        Month += 1
    if numberOfDays >= 31: 
        numberOfDays -= 31
        Month += 1
    if numberOfDays >= 30: 
        numberOfDays -= 30
        Month += 1
    if numberOfDays >= 31: 
        numberOfDays -= 31
        Month += 1
    if numberOfDays >= 30: 
        numberOfDays -= 30
        Month += 1
    if numberOfDays >= 31: 
        numberOfDays -= 31
        Month = 1
        Year += 1

Day += numberOfDays
print(f"{Day} {Month} {Year}")
