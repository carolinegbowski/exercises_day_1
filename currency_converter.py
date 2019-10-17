def currency_converter(dollars): 
    dollars = float(dollars)
    cents = dollars * 100 
    cents = int(cents)
    hundreds = cents // 10000
    remainder = cents % 10000
    fifties = remainder // 5000
    remainder = remainder % 5000
    twenties = remainder // 2000
    remainder = remainder % 2000
    tens = remainder // 1000
    remainder = remainder % 1000
    fives = remainder // 500
    remainder = remainder % 500
    ones = remainder // 100
    remainder = remainder % 100
    quarters = remainder // 25
    remainder = remainder % 25
    dimes = remainder // 10
    remainder = remainder % 10
    nickels = remainder // 5
    remainder = remainder % 5
    pennies = remainder // 1 
    if hundreds > 0:
        print(str(hundreds) + " $100")
    if fifties > 0:
        print(str(fifties) + " $50")
    if twenties > 0:
        print(str(twenties) + " $20")
    if tens > 0:
        print(str(tens) + " $10")
    if fives > 0:
        print(str(fives) + " $5")
    if ones > 0:
        print(str(ones) + " $1")
    if quarters > 0:
        print(str(quarters) + " quarters")
    if dimes > 0:
        print(str(dimes) + " dimes")
    if nickels > 0:
        print(str(nickels) + " nickels")
    if pennies > 0:
        print(str(pennies) + " pennies")
    return

currency_converter(12.33)
